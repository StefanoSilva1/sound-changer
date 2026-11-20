from dataclasses import dataclass
import json
from pathlib import Path
import unicodedata #for character normalization, which is important for consistent text processing (otherwise identical looking characters might be read in two different ways by the computer)

@dataclass(frozen=True) #keeps the dataclass from changing
class GraphemeToken: #matching the structure found in the langauge JSON
    grapheme: str
    ipa: str
    phoneme_class: str
    features: tuple[str, ...] #we use tuples instead of list to keep it immutable

class OrthographyParser:
    def __init__(self, profile_path: str | Path, strict: bool = True):
        self.profile_path = Path(profile_path)
        self.strict = strict

        with self.profile_path.open("r", encoding="utf-8") as f:
            data = json.loads(unicodedata.normalize("NFC", f.read()))

        self.lang_code: str = data.get("lang_code", "") #use later for etymology changelog
        self.transcription: dict = data.get("transcription", {})
        inventory: list[dict] = data.get("inventory", [])

        self.entries: list[GraphemeToken] = sorted(
            (
                GraphemeToken( #matches our dataclass/json
                    grapheme=unicodedata.normalize("NFC", item["grapheme"]),ipa=unicodedata.normalize("NFC", item["ipa"]),
                    phoneme_class=item.get("class", "Other"),
                    features=tuple(item.get("features", [])),
                )
                for item in inventory
            ),
            key=lambda t: len(t.grapheme), #key means "sorting criteria" and we are sorting by the length of the grapheme
            reverse=True, #this puts longest graphemes first, so that we match them before shorter ones when parsing text
        )
    def GraphemeTokenize(self, text: str, lowercase: bool = False) -> list[GraphemeToken]:
        # Normalize the text to ensure consistent processing USE NFC -- check [important-information.md] for more information
        source = unicodedata.normalize("NFC", text) 
        if lowercase:
            source = source.lower() #this is useful for languages that don't have case distinctions, but for a language like klingon where case is important, you might want to keep it as is. This is why we have a lowercase toggle.
            #we also want to avoid lowercasing the names of Groups, since the parser distinguishes groups from literals on the basis of capitalization.
        GraphemeTokens: list[GraphemeToken] = []
        i = 0
        n = len(source)

        while i < n:
            matched = None #do this so it has an immediate value, preventing errors if no match is found
            for entry in self.entries:
                g = entry.grapheme
                # This will take the current position, and check the graphemes in the order we sorted during init (longest first). Imagine that the lemma were <bring> and two of our graphemes were <br> and <b>. The loop will smartly lookahead and match <br> first, instead of <b>, which would be incorrect.
                if source.startswith(g, i):
                    matched = entry 
                    break

            if matched is not None:
                GraphemeTokens.append(matched)
                i += len(matched.grapheme) #move the index forward by the length of the matched grapheme
            elif self.strict: # if strict, raise error
                raise ValueError(
                    f"Unrecognized grapheme at position {i}: '{source[i]}' for profile '{self.lang_code}', at '{self.profile_path}'"
                )
            else: # if not strict, just add the character as a GraphemeToken with default values
                ch = source[i]
                GraphemeTokens.append(
                    GraphemeToken(
                        grapheme=ch, 
                        ipa=ch, 
                        phoneme_class="Other", 
                        features=(),
                    )
                )
                i += 1

        return GraphemeTokens

    def to_ipa(self, text: str, lowercase: bool = False, separator: str = "") -> str:
        return separator.join(GraphemeToken.ipa for GraphemeToken in self.GraphemeTokenize(text, lowercase=lowercase))

if __name__ == "__main__":
    parser = OrthographyParser("MOPX.json", strict=True)

    orthography_samples = [
    "bə-gi",
    "do:yin",
    "kjagju",
    "kjaimjʌnə",
    "nu-bə",
    "yə-igjə",
    #"'-bə", 
    # (no symbol ' defined in the JSON, so this will throw an error in strict mode)
    "tʃa:řo:m",
    "yæ:kju:gi",
    "pɪdʒʌ-nə",
    #"Tʃa:ř", 
    # (no symbol T defined in the JSON, so this will throw an error in strict mode (if lowercasing isn't turned on))
    "pi-kju",
]

    for word in orthography_samples:
        GraphemeTokens = parser.GraphemeTokenize(word)
        print(f"Word: {word!r} -> /{parser.to_ipa(word)}/ GraphemeTokens={[GraphemeToken.grapheme for GraphemeToken in GraphemeTokens]}")