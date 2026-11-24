from dataclasses import dataclass
import json
from pathlib import Path
import unicodedata
import re

@dataclass(frozen=True)
class GraphemeToken: #matches JSON structure
    grapheme: str
    ipa: str
    phoneme_class: str
    features: tuple[str, ...]

@dataclass(frozen=True)
class GroupToken:
    name: str
    type: str
    contents: tuple[dict, ...]

@dataclass(frozen=True)
class ChangeToken:
    target: str
    result: str
    environment: dict
    stops: tuple[str, ...] = tuple() #default to empty tuple if not provided

@dataclass(frozen=True)
class EnvironmentToken:
    left: str
    right: str
    type: str

@dataclass(frozen=True)
class IntermediateRuleToken:
    change: str
    environment: list[str]
    exceptions: list[str]
    stops: list[str]
    origin: str

class IPAParser:
    def __init__(self, profile_path: str | Path, strict: bool = False):
        # Default to "false" so that 'unused' IPA characters just go through
        self.profile_path = Path(profile_path)
        self.strict = strict

        with self.profile_path.open("r", encoding="utf-8") as f:
            data = json.loads(unicodedata.normalize("NFC", f.read()))
            #we can just normalize once, after we get input from the file, instead of normalizing each individual grapheme and ipa in the inventory. This is more efficient and also ensures that we don't have any inconsistencies in normalization between the graphemes and the IPA.

        self.lang_code: str = data.get("lang_code", "")
        self.transcription: dict = data.get("transcription",  {})
        
        targets: list[dict] = [] #the things we will end up searching for
        grouped_targets: list[dict] = [] #things we might need to search for, but which are grouped together in a rule group (like S and Q in MOPX)
        grouped_rules: list[dict] = [] #the rules that are grouped together in a rule group

        rule_groups: dict = data.get("rule_groups", {})

        for name, item in rule_groups.items():
            if item.get("type") == "IPA_to_Orthography":
                for group in item["groups"]:
                    parsed_group: dict = self.make_group_tokens(group)
                    grouped_targets.extend(parsed_group)
                for rule in item["rules"]:
                    parsed_rule: dict = self.make_rule_tokens(rule)
                    grouped_rules.append(parsed_rule)

        # print(f"Grouped targets: {grouped_targets}")
        #print(f"Grouped rules: {grouped_rules}")

        change_operators: list[str] = sorted(
            data["personal_settings"]["operators"]["assignment"],
            key=len,
            reverse=True
        )

        target_operators: list[str] = sorted(
            data["personal_settings"]["operators"]["target"],
            key=len,
            reverse=True
        )

        for token in grouped_rules:
            change = token.change

            for operator in change_operators:
                if operator in change:
                    fields = change.split(operator)
                    target = fields[0].strip()
                    result = fields[1].strip()
                    break

            environment_tokens = self.make_environment_tokens(
                token.environment,
                "environment",
                target_operators
            )

            exception_tokens = self.make_environment_tokens(
                token.exceptions,
                "exception",
                target_operators
            )

            all_environment_tokens = environment_tokens + exception_tokens

            x = ChangeToken(
                target = target,
                result = result,
                environment = all_environment_tokens,
                stops = tuple(token.stops)
            )
            grouped_targets.append(x)

        print(f"Final grouped targets: {grouped_targets}")

    def make_environment_tokens(
            self,
            conditions: list[str],
            token_type: str,
            target_operators: list[str]
    ) -> list[EnvironmentToken]:

        environment_tokens:list[EnvironmentToken] = []

        for symbol in target_operators:
            for item in conditions:
                if symbol in item:
                    fields = item.split(symbol)
                    left = fields[0].strip()
                    right = fields[1].strip()

                    left_options = expand_optionals(left)
                    right_options = expand_optionals(right)

                    for left_option in left_options:
                        for right_option in right_options:
                            environment_tokens.append(
                                EnvironmentToken(
                                    left=left_option,
                                    right=right_option,
                                    type=token_type
                                )
                            )

        return environment_tokens

    def make_group_tokens(self, group:str) -> dict:
        group_name:str = group[0]
        if group[1] == "*":
            group_type:str = "change"
        else:
            group_type:str = "standard"
        group_content: list[dict] = []
        contents: list[str] = group.split("{", 1)[1].split("}", 1)[0].split(";")
        # we can only split multiple times because we know that the first "{" and the last "}" are the ones that matter. If there are any other "{" or "}" in the middle, they will be part of the contents, and we don't want to split on those. Additionally, we can do the split again on the comma only because the first part returned only one string rather than a list
        contents = [item.strip() for item in contents]
        for item in contents:
            sides: list[str] = item.split(">")
            sides = [character.strip() for character in sides]
            ipa: list[str] = []
            ipa.append(sides[0])
            grapheme: list[str] = []
            grapheme.append(sides[1])
            # environments currently not supported, but we will keep the structure to add it later
            group_content.append(ChangeToken(
                target=ipa,
                result=grapheme,
                environment={}
            ))

        group_return: list[GroupToken] = []
        group_return.append(GroupToken(
            name=group_name,
            type=group_type,
            contents=group_content
        ))

        return group_return

    def make_rule_tokens(self, rule:str) -> dict:

        contents: list[str] = rule.split("///")
        stops: list[str] = [part.strip() for part in contents[1:]]

        contents = contents[0].split("//")
        exceptions: list[str] = [part.strip() for part in contents[1:]]

        contents = contents[0].split("/")
        environment: list[str] = []
        int_environment: list[str] = [part.strip() for part in contents[1:]]
        for each in int_environment:
            part: list[str] = each.split(",") #split the environment into a list of strings, so that we can process each part separately
            environment.extend(part)
        environment = [item.strip() for item in environment]

        change: str = contents[0].strip()

        rule_return: IntermediateRuleToken = IntermediateRuleToken(
            change=change,
            environment=environment,
            exceptions=exceptions,
            stops=stops,
            origin=rule
        )

        return rule_return
        
def expand_optionals(pattern:str) -> list[str]:
        match = re.search(r"\(([^()]*)\)", pattern)
        if not match:
            return [pattern]
        with_optional = pattern[:match.start()] + match.group(1) + pattern[match.end():]
        without_optional = pattern[:match.start()] + pattern[match.end():]
        return list(dict.fromkeys(expand_optionals(with_optional) + expand_optionals(without_optional)))  # Remove duplicates while preserving order

if __name__ == "__main__":
    parser = IPAParser("MOPX.json", strict=False)