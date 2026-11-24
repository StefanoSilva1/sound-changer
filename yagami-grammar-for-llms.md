# YAGAMI — LLM GRAMMAR & PARSING REFERENCE SPEC

**Version:** Updated working specification  
**Purpose:** Authoritative parsing, translation, grammatical analysis, and language-generation reference for LLMs.

## 0. Instructions for interpreting Yagami

This document is the primary authority for interpreting Yagami. Follow its rules rather than automatically mapping Yagami constructions onto English grammar.

When parsing or generating Yagami:

1. Preserve the distinction between grammatical structure and English translation.
2. Treat roots as omnicategorical unless derivation establishes a particular function.
3. Distinguish grammatical person from social alignment.
4. Distinguish social involvement or affectedness from perspective marking.
5. Interpret verbal endings according to their morphological position and predicate type.
6. Interpret compounds according to the relationships between their components.
7. Pay attention to punctuation, especially commas, because it can distinguish phrase-level modification from discourse-level modification.
8. Use discourse context when interpreting ellipsis, recurring modifiers, and ambiguous references.
9. Do not invent rules for unresolved grammatical areas.
10. Explicitly flag apparent grammatical errors, ambiguities, and inconsistencies rather than silently correcting them.

**Evidence hierarchy:**

- **Established:** Explicitly specified or directly confirmed by the language creator.
- **Observed:** Demonstrated in examples but not necessarily established as a universal rule.
- **Provisional:** A plausible analysis awaiting further examples or confirmation.
- **Unresolved:** No reliable rule has been established.

Do not promote observed or provisional interpretations to established rules without confirmation.

---

# 1. Language identity and design

Yagami is an engineered, minimalist, heavily agglutinative constructed language designed for high-speed drafting, linguistic experimentation, and gradual lexical autonomy.

Its name means approximately "conlanging in general."

## 1.1 Design influences

- **Japanese:** SOV syntax, topic-comment framing, sentence-final question particle `ka`, desiderative `-tai`, comparative `-oːki-`, and lexical roots such as `kyo`, `ima`, and `tabe`.
- **Portuguese/Romance:** Aspectual `-ʒ`, command/deontic clitics `t'-` and `n'-`, comitative `co-`, verbalizer `-r`, and clipped roots.
- **English:** Temporary lexical scaffold, plural `-s`, and phonotactic influence on epenthesis.
- **Original systems:** Spatial-social deixis, social-alignment verb agreement, fixed five-slot verb morphology, omnicategorical roots, ontological nominal suffixes, and perspective-oriented predicate marking.

## 1.2 Core philosophy

Yagami favors broad, flexible vocabulary while making particularly important social and emotional distinctions with greater precision.

Its vocabulary is compositional and productive. Roots can combine with semantic suffixes to create broad categories, while lexicalized words can develop narrower conventional meanings.

Yagami organizes reference around relationships:

- Physical relationships.
- Social relationships.
- Contextual relationships.
- The relationship between an experiencer and an event.
- The standpoint from which a proposition is interpreted.

The language should be interpreted according to its established rules rather than automatically mapped onto English grammatical categories.

---

# 2. Phonology and orthography

## 2.1 Syllable structure

The general syllable template is:

`(s)C(C)(G)V(V)(C)(C)(s)`

- Optional initial `s`.
- Up to two consonants in the onset.
- Optional glide `y` or `w`.
- Single vowel, long vowel, or diphthong.
- Up to two consonants in the coda.
- Final `-s` is the plural suffix.

## 2.2 Sound inventory

The consonant inventory includes standard English consonants except /θ/ and /ð/, with additional sounds:

- /x/
- /ʒ/
- /ɲ/, written `ñ`
- IPA /r/

The vowel inventory includes:

`a e i o u æ ɪ ɔ ʌ ə ɛ ʊ ɚ`

Long vowels are marked with `ː`, or sometimes a colon.

## 2.3 Morpheme boundaries

Hyphens and apostrophes represent glottal stops in pronunciation.

They are not merely explanatory separators. They mark real phonological boundaries.

Over time, these boundaries may erode, allowing phonetic changes and lexicalization.

A hyphenated form remains transparently compositional. A form written without the hyphen may have undergone lexicalization and acquired a narrower conventional meaning.

Hyphens can also indicate that two elements are tightly associated, as in `koi-mim` ("my idea").

Do not automatically treat a hyphen as an optional written separator.

## 2.4 Epenthesis

Epenthetic vowels repair consonant clusters that violate the language's phonotactic constraints.

Two vowel-selection principles are established:

1. **Word-level epenthesis:** The inserted vowel copies the first vowel in the word.
2. **Person-marker epenthesis:** When a vowel is needed to accommodate a person/social-alignment ending, it copies the vowel associated with tense.

These are distinct environments with different vowel sources.

The system should not automatically insert schwa.

An apparent form such as `-ak` may represent `-a` plus `-k`, with an epenthetic vowel. Do not reject such forms merely because they appear to have an unexpected vowel.

---

# 3. Verb morphology

## 3.1 Five-slot verb chain

The standard verb structure is:

`[Root] + [Helpers] + [Negation] + [Tense/Aspect] + [Social alignment]`

| Slot | Function | Examples |
|---|---|---|
| 1 | Root | `har`, `faz`, `nunar`, `taber` |
| 2 | Helpers | `-tai`, `-oːki-`, `aʃkei` |
| 3 | Negation | `-nə-` |
| 4 | Tense/aspect | `-i`, `-a`, `-an`, `-ʒ`, `-r` |
| 5 | Social alignment | `-m`, `-t`, `-k` |

The order is fixed.

Do not confuse a helper, tense marker, or social-alignment marker with an independent lexical root.

## 3.2 Helpers

Helpers modify the meaning of the predicate.

- `-tai`: Want/desire.
- `-oːki-`: More/comparative; can also intensify a meaning as "big" or "very."
- `aʃkei`: Seem/appear.

The interpretation of a helper depends on the root and the relationship between the elements.

Examples:

- `want + more + not + past + ingroup`: I didn't want any more.
- `eat + more + want + not + past + ingroup`: I didn't want to eat more.
- `motivation-oːki`: Can express being very or highly motivated, rather than necessarily being more motivated than something else.

The helper sequence must not be interpreted independently of its predicate.

In particular, do not force a comparative interpretation of `-oːki-` when the context supports an intensifying interpretation.

## 3.3 Negation

`-nə-` occupies slot 3.

It marks negation within the verb chain.

Negation may coexist with an independently negative adverb or expression.

For example:

`Nunk [motivation]-oːki-nə-ilm`

Intended meaning: "I have never been very motivated."

Here:

- `Nunk` means "never."
- `-nə-` marks verbal negation.
- Their coexistence does not cancel the negative meaning.

**Observed:** Yagami permits this negative-concord interpretation. Do not automatically apply English double-negative logic.

## 3.4 Tense and aspect

| Form | Meaning |
|---|---|
| `-i` | Past |
| `-a` | Nonpast/present |
| `-an` | Future |
| `-ʒ` | Proximative / close-in-time aspect |
| `-iʒ` | Just did |
| `-aʒ` | About to happen / coming to pass |
| `-il` | Past with present relevance; can correspond to "have been" |
| `-r` | Present-tense verbal ending |

The precise vowel alternation of future forms across social-alignment endings remains to be established.

The proximative aspect relates an event to the immediate temporal context, allowing both recent-past and imminent interpretations.

### The present-tense `-r`

`-r` has two distinct grammatical functions:

1. It is the usual verbalizer used to derive verbs from roots.
2. It can function as a present-tense verbal ending in the verb chain.

These functions must not be conflated.

The verbalizer derives a verb from a root. The present-tense ending contributes temporal information to an already verbal predicate.

The form and its function must be interpreted according to morphological position and context.

The `-arm` construction discussed below is an important example of the present-tense/perspective use.

### The `-il` form

`-il` is a newly established past form with present relevance.

It can express an experience or state extending into the present, including "have been."

Example:

`[motivation]-oːki-nə-ilm`

"I have never been very motivated."

Its full aspectual distribution remains provisional.

## 3.5 Social-alignment agreement

The final verb endings are conventionally interpreted as person markers, but their underlying function is different.

They encode the speaker's social alignment with the relevant participant or group.

| Ending | Underlying meaning | Conventional interpretation |
|---|---|---|
| `-m` | Ingroup | I / we |
| `-t` | Outgroup | You / you plural |
| `-k` | Socially distant group | They / those people |

Number is not the defining distinction.

For example, `-m` can refer to a group and mean "we" when all relevant members belong to the speaker's ingroup.

The endings therefore represent social-alignment agreement rather than ordinary grammatical person agreement.

### A. Ordinary social-alignment marking

In ordinary constructions, the ending identifies the socially aligned participant or group relevant to the predicate.

It may identify an experiencer, affected participant, or other relevant participant.

Examples:

`bene-nə-am`

"This isn't beneficial to me/us."

`har-tai-am`

"I/we want [the relevant thing to happen]."

The ingroup is the participant whose interests, desire, or involvement are relevant.

Do not assume that every `-m` construction means that the ingroup is the agent performing an action.

### B. Distinguishing `-am` and `-arm`

**Important: `-am` and `-arm` must be kept distinct.**

They are not interchangeable forms, and `-arm` should not replace or erase the older `-am` construction.

The emerging distinction is:

| Form | Core interpretation |
|---|---|
| `-am` | Ingroup involvement, association, affectedness, or experiencer alignment |
| `-arm` | Ingroup perspective or standpoint |

`-am` relates a situation to the ingroup as a participant in, affected party to, or experiencer of that situation.

`-arm` relates a proposition to the standpoint from which the ingroup understands, experiences, or evaluates it.

The distinction can be summarized as:

- `-am`: Whose interests or involvement are relevant?
- `-arm`: From whose perspective is the proposition interpreted?

### C. The perspective-oriented `-arm` construction

`-arm` is associated with the newly established present-tense `-r` and ingroup `-m` combination.

Its semantic interpretation is perspective-oriented.

It can identify the ingroup as:

- Experiencer: the group experiencing a state or event.
- Evaluator: the group judging something beneficial, difficult, correct, or otherwise.
- Standpoint: the group whose perspective provides the relevant reference point.

Examples:

`Yagami [grammar]-[difficult]-arm`

"I find Yagami grammar difficult."

The difficulty is presented according to the speaker's perspective. It is not necessarily an objective claim that Yagami grammar is inherently difficult.

`Totemo, [electric-brain] Yagami [complex]-aʒam`

"I feel the Yagami program keeps becoming more complicated."

The ingroup ending identifies the speaker as the relevant evaluator or experiencer.

`Demo, [parts] [many]-arm`

An observed construction in which the ingroup perspective is relevant to the present evaluation.

**Do not reduce `-arm` to "subjective judgment."** Perspective is broader than evaluation. Depending on predicate type, it can manifest as an experiencer, evaluator, or standpoint.

### D. Scope of the distinction

The `-am` versus `-arm` distinction is established as a meaningful contrast in the examples discussed.

However, the complete distribution of this contrast remains provisional.

Do not automatically assume that every social alignment or tense has a corresponding `-ar...` form.

Potential forms such as `-art`, `-ark`, `-irm`, or other combinations have not yet been established as productive paradigms.

Do not generate or prescribe these forms without further confirmation.

### E. Relevant predicates

Predicates where experiencer or evaluator marking is especially relevant include:

- `nunar`
- `aʃkei`
- `bene`
- `t'har-`
- Predicates describing difficulty, complexity, motivation, or desire.

The distinction between agent, experiencer, affected participant, and evaluator must be maintained.

## 3.6 Command and deontic clitics

`t'-` and `n'-` are clitic command-form markers, not prefixes occupying one of the five verb slots.

- `t'` + bare root: Positive imperative.
- `n'` + bare root: Negative imperative.
- `t'` + conjugated verb: Deontic obligation or stance.
- `n'` provides the corresponding negative command construction.

The conjugated verb retains its ordinary five-slot structure.

Example from the original specification:

`t'har-am`

"I feel that something should have/exist."

The exact interpretation of this older construction should be retained rather than automatically replaced by the newer `-arm` perspective construction.

### Deontic temporal distinctions

Three distinct constructions have been established:

| Construction | Meaning |
|---|---|
| `t'[verb]-arm` | I must [verb]; pressing, immediate necessity |
| `t'[verb]-aʒam` | I should [verb] soon |
| `t'[verb]-anam` | I will [verb] later |

These are semantically distinct.

- `-arm`: Something needs to happen immediately. The necessity is pressing.
- `-aʒam`: Something ought to happen soon, but the necessity is less immediate.
- `-anam`: A future intention or commitment to do something later.

Example:

`Totemo, t'[try]-arm`

"I must keep trying."

`Totemo` supplies the continuing/recurring interpretation, while the deontic construction expresses immediate necessity.

Do not collapse these three constructions into a generic meaning of "should."

## 3.7 Gnomic aspect

`-ok` marks general truths, universal statements, and gnomic propositions.

On verbal stems ending in `-r`, the verbalizer is dropped before `-ok`.

Example:

`kyaka wrong-ok`

"One errs."

## 3.8 Resultative/inchoative framing

Clause-initial `So ima` ("so now") can combine with proximative `-aʒ` to express a state or rule taking effect now as a result of preceding context.

---

# 4. Spatial-social deixis and pronouns

## 4.1 Fundamental principle

Yagami's pronominal system is not fundamentally organized around grammatical person.

It combines two independent dimensions:

1. Physical distance relative to the conversational participants.
2. Social distance relative to the speaker's current ingroup.

The resulting forms describe relationships, not permanent identities.

## 4.2 Physical distance

| Prefix | Meaning |
|---|---|
| `mi-` | Near the speaker's area |
| `tu-` | Near the listener's area |
| `kya-` | Away from both participants |

## 4.3 Social distance

| Suffix | Meaning |
|---|---|
| `-m` | Ingroup |
| `-t` | Outgroup |
| `-k` | Distant, foreign, unintegrated, or outcast |

The social categories are elastic and context-dependent.

They do not permanently classify people according to kinship, familiarity, or geographical location.

A speaker determines the relevant ingroup boundary in the current social situation.

For example:

- When speaking to a brother, the speaker may classify themself as `-m` and their parents as `-k`.
- When speaking to neighbors, the speaker may classify their family as `-m` and the neighbors as `-t`.
- When speaking among those neighbors, the neighbors may become `-m`, while people across town become `-k`.

The categories describe the speaker's current social alignment.

They can also express deliberate exclusion. A person can classify themself as socially distant from a group they are discussing.

## 4.4 The nine combinations

| Physical / Social | `-m` Ingroup | `-t` Outgroup | `-k` Distant |
|---|---|---|---|
| `mi-` Near speaker | `mim` | `mit` | `mik` |
| `tu-` Near listener | `tum` | `tut` | `tuk` |
| `kya-` Away from both | `kyam` | `kyat` | `kyak` |

The nine combinations are not necessarily equally frequent.

## 4.5 Conventional interpretations

The literal compositional meanings are broader than their ordinary translations.

| Form | Usual interpretation |
|---|---|
| `mim` | I / me / my |
| `tum` | You / yours |
| `kyam` | This / that / he / she / it / previously mentioned thing |
| `kyat` | That thing or person associated with the outgroup |
| `kyak` | That socially distant, foreign, or alien thing or person |

These are conventional interpretations, not exhaustive definitions.

For example, `mim` literally describes one ingroup person closely aligned with the speaker. Its ordinary use as "I" follows from that meaning.

Likewise, `kyam` is not inherently a third-person pronoun. Its conventional use as a demonstrative, anaphoric reference, or third-person pronoun develops from its underlying spatial-social meaning.

## 4.6 Possession versus reference

Possession and association are distinct from demonstrative reference.

- `mim`: My / associated with me.
- `tum`: Yours / associated with you.
- `kyam`: That previously mentioned or contextually identified thing, without necessarily claiming ownership.

Examples:

- `koi mim`: My idea or plan.
- `koi tum`: Your idea or plan.
- `koi kyam`: That idea or plan already being discussed.
- `koi kyak`: That alien, foreign, or socially distant idea.

The choice of `kyak` can convey dismissal or social rejection without requiring a dedicated insult word.

A tightly bound form such as `koi-mim` can also mean "my idea." The hyphen indicates a close association.

Do not assume that every possessive or associative construction must be written as two independent words.

## 4.7 Plural and gender

The pronoun forms can take plural `-s`.

Optional gender suffixes:

- `-er`: Female.
- `-en`: Male.

These are generally unnecessary unless gender needs to be specified.

## 4.8 Social alignment and group identity

The system can express changing circles of solidarity.

A person may classify someone as `-k` in one conversation and `-m` in another, depending on the group being contrasted with the outside world.

The underlying idea resembles shifting circles of allegiance:

- Me against my brother.
- Me and my brother against my cousin.
- Me and my cousin against the world.

This is not merely a system of politeness. It encodes social identification, belonging, exclusion, and alignment.

---

# 5. Syntax, nominals, and discourse

## 5.1 Basic word order

Yagami uses SOV word order and topic-prominent framing.

The topic establishes what is being discussed. Other arguments and modifiers generally precede the final verb.

## 5.2 Experiencer/judge alignment

Certain predicates mark the experiencer or judge in the final verb ending.

This person need not be the grammatical subject or topic.

Examples:

`Nene comim nunar-ik`

"The baby enjoyed spending time with me."

The baby is the third-person experiencer.

`Nene comim nunar-im`

"As for the baby, I enjoyed spending time with her."

The speaker is the experiencer.

This distinction is important when parsing psychological, evaluative, and deontic predicates.

It also illustrates why the social-alignment ending should not automatically be translated as an ordinary subject pronoun.

## 5.3 Questions

Sentence-final `ka` turns a statement into a question without requiring word-order inversion.

## 5.4 Nominal phrase order

Established tendencies:

- Articles and numerals precede the head.
- Demonstratives follow the head.
- Possessors follow the head.
- Modifiers and relative-like phrases follow the head.

Examples of relevant elements:

- `õs`: Plural article "the."
- `dois`: Two.
- `kyam`: Demonstrative.
- `-mim`: Possessive/associative reference.

Plural `-s` attaches to nouns and pronouns.

## 5.5 Comitative

`co-` attaches to personal pronouns to mean "with [person]."

It is intended for animate or personal accompaniment.

Examples:

- `comim`: With me.
- `comims`: With us.

## 5.6 Discourse-level modifiers and punctuation

Commas have a grammatical and interpretive function in Yagami.

They can distinguish a discourse-level modifier from a modifier integrated into a nominal phrase.

A comma is not merely a pause or stylistic choice.

### A. Independent discourse modifiers

A word separated from the following proposition by a comma can operate at the discourse or clause level.

Examples:

`Totemo, X`

"Always/continually, X."

`Demo, X`

"But, X."

`So, X`

"So/therefore, X."

These expressions frame the proposition that follows.

They can establish continuity, contrast, or consequence without necessarily becoming constituents of the following noun phrase.

### B. Integrated nominal modifiers

Without a discourse boundary, a similar-looking form can function within a noun phrase.

Example:

`kois totemos`

"All ideas."

Here, `totemos` functions as a nominal quantifier modifying `kois`.

### C. Important contrast

| Construction | Function |
|---|---|
| `Totemo, X` | Proposition-level recurring/continuing modifier |
| `kois totemos` | Nominal quantification: all ideas |

Do not translate both forms as "always."

The distinction is syntactic and semantic, not merely orthographic.

### D. Discourse carryover

A discourse-level modifier may establish an interpretation that continues across subsequent clauses.

For example, `Totemo` can establish a recurring or continuing context that remains relevant to the next proposition.

Do not automatically assume that every subsequent clause must repeat the modifier explicitly.

However, the exact rules governing ellipsis and the scope of discourse carryover remain to be established.

---

# 6. Omnicategorical roots and derivation

## 6.1 Omnicategorical words

Yagami roots are omnicategorical.

A root is not inherently restricted to nouns, verbs, adjectives, or another grammatical category.

The verbalizer `-r` is the usual way to derive verbs.

Examples:

- `tabe`: Ingestible substance.
- `taber`: Ingest.

The same `-r` form can also function as a present-tense verbal ending in the appropriate morphological context. These uses must be distinguished.

## 6.2 Verbal orientation: `-r` versus `faz`

When a root has multiple possible verbal interpretations, Yagami distinguishes an undergoer-oriented interpretation from an agent-oriented interpretation.

The productive distinction is:

- **Plain verbalization with `-r`:** Takes the more undergoer-oriented or passive-oriented interpretation.
- **Root + `faz`:** Takes the more agent-oriented, active, or causative interpretation.

Examples:

| Construction | Meaning |
|---|---|
| `taber` | Eat / ingest |
| `taber faz` | Cook / prepare food |
| `konpir` | Read nonfiction |
| `konpi faz` | Write nonfiction |

The distinction should be understood semantically rather than as a strict grammatical passive-versus-active voice opposition.

The root identifies the underlying activity or conceptual domain. `faz` introduces the active creation or production interpretation.

### Parsing instruction

When a root has both interpretations:

1. Prefer the undergoer-oriented interpretation for the plain verbalized form.
2. Prefer the agent-oriented interpretation when `faz` is used.
3. Do not assume that the English dictionary meaning of the root determines the direction of the action.
4. Do not treat examples such as `taber faz` and `konpi faz` as isolated lexical exceptions.

This rule applies when the root supports the distinction. It should not be forced onto roots where an active/undergoer contrast is not meaningful.

## 6.3 Ontological suffixes

Yagami uses semantic suffixes to classify entities associated with a root.

| Suffix | Meaning |
|---|---|
| `-koi` | Abstract thing, concept, choice, or option |
| `-bə` | Physical object associated with the root |
| `-lug` | Physical place or location associated with the root |

These suffixes can also function independently.

Their meanings are relatively narrow, but the roots they attach to can be broad.

Examples:

- `tabe-bə`: Physical objects associated with ingestion, such as dishes, cookware, and utensils.
- `tabe-koi`: Ingestion as an abstract concept.
- `tabe-lug`: A place associated with ingestion.

`-bə` does not mean the agent or undergoer of an action. It classifies physical objects associated with the root.

## 6.4 Productive compounds and lexicalization

A hyphenated construction remains transparent and productive.

For example, `tabe-bə` has a broad compositional meaning: physical objects associated with ingestion.

A lexicalized form without the hyphen, such as `tabebə`, may acquire a narrower conventional meaning, such as "tableware."

This reflects the erosion of morpheme boundaries and subsequent semantic narrowing.

The distinction between productive compounds and lexicalized vocabulary is intentional.

## 6.5 Tight association and possession

A hyphen can indicate a particularly close association between elements.

Example:

`koi-mim`

"My idea."

The construction should not automatically be treated as an ordinary juxtaposition of two independent words.

Its tight binding expresses the relationship between the concept and the associated person.

---

# 7. Current lexicon

The lexicon below combines the original inventory with vocabulary established or used during the example exercises.

Placeholder roots are identified separately. Do not treat placeholders as confirmed permanent lexical entries.

## 7.1 Function words and pronouns

| Form | Meaning |
|---|---|
| `kyam` | Demonstrative / third-person reference |
| `kyaka` | Indefinite, interrogative, or generic nominal: what, which, one |
| `mim` | I / me / my |
| `tum` | You / yours |
| `õs` | Plural article, "the" |
| `dois` | Two |
| `co-` | With-person prefix |
| `ka` | Question particle |
| `nə` | Negation |
| `t'-` | Command/deontic marker |
| `n'-` | Negative command marker |
| `So` | Clause-initial so/therefore |
| `Mo` | Clause-initial also |
| `Demo` | But; contrastive conjunction |

## 7.2 Nouns and time

| Form | Meaning |
|---|---|
| `koi` | Thing, option, choice, abstract concept |
| `-koi` | Abstract thing, concept, choice, or option |
| `-bə` | Physical object associated with root |
| `-lug` | Physical place/location associated with root |
| `nene` | Baby |
| `kyo` | Today |
| `ima` | Now |
| `tabe` | Ingestible substance |
| `konpi` | Nonfiction, such as a book or essay |
| `cause` | The thing that leads to an effect; noun |
| `electric-brain` | Computer or computer program |

## 7.3 Discourse and quantification

| Form | Meaning / function |
|---|---|
| `Totemo` | Always, continually, recurring; proposition-level modifier when separated by a comma |
| `totemos` | All; nominal quantifier |
| `Nunk` | Never |
| `ihi` | One; very few |

The distinction between `Totemo` and `totemos` is important.

`Totemo, X` modifies the proposition.

`kois totemos` means "all ideas."

Do not assume `totemos` is simply a plural form of `Totemo`.

## 7.4 Verbs and helpers

| Form | Meaning |
|---|---|
| `har` | Have, get, obtain, exist |
| `faz` | Create, make |
| `nunar` | Experience pleasure, enjoy, be pleasing |
| `aʃkei` | Seem, appear |
| `bene` | Helpful, beneficial |
| `taber` | Ingest |
| `wrong` | Err, be wrong |
| `differ` | Differ, be distinct |
| `-tai-` | Want |
| `-oːki-` | More/comparative; also intensifying |
| `-ok` | Gnomic |
| `-i` | Past |
| `-a` | Nonpast |
| `-an` | Future |
| `-ʒ` | Proximative |
| `-iʒ` | Just did |
| `-aʒ` | About to happen / coming to pass |
| `-il` | Past with present relevance |
| `-r` | Verbalizer; also present-tense verbal ending in its separate grammatical use |
| `-m/-t/-k` | Social-alignment agreement |

## 7.5 Placeholder vocabulary from example exercises

The following English forms have appeared as placeholders in grammatical examples:

- `[grammar]`
- `[difficult]`
- `[complex]`
- `[motivation]`
- `[focus]`
- `[ponder]`
- `[try]`
- `[parts]`

They represent concepts being tested, not necessarily established Yagami roots.

When parsing a sentence containing bracketed placeholders, preserve the intended placeholder meaning rather than inventing a Yagami lexical entry.

---

# 8. Example constructions and interpretations

These examples demonstrate the current grammatical understanding. They should be used as parsing precedents.

## 8.1 Continuing proposition

`Totemo, koi-mim complex-aʒak`

Approximate meaning:

"My ideas keep becoming complicated."

Important observations:

- `Totemo` is proposition-level because of the comma.
- `koi-mim` is a tightly bound associative/possessive expression.
- `-aʒ` expresses proximative or coming-to-pass meaning.
- The final social alignment must be interpreted according to its grammatical role, not automatically as a first-person subject.

## 8.2 Continuing problem

`Problem-aʒam`

In the preceding discourse, this can express something like:

"That keeps becoming a problem for me."

The continuing interpretation can be carried over from `Totemo` in the preceding context.

The exact ellipsis mechanism remains provisional.

## 8.3 Deontic focus

`ihi t'[focus]-aʒam`

An example involving the idea of focusing on one or very few things.

`ihi` can mean "one" or "very few." Its use can be elliptical when the intended nominal is recoverable from context.

The deontic construction expresses an obligation or recommendation to act soon, not an immediate necessity.

## 8.4 Negative motivation

`Nunk [motivation]-oːki-nə-ilm`

Intended meaning:

"I have never been very motivated."

Important observations:

- `Nunk` means never.
- `-oːki-` intensifies the predicate.
- `-nə-` marks verbal negation.
- `-il` provides the past-with-present-relevance interpretation.
- Negative concord is retained.

## 8.5 Pondering a cause

`[often], cause [ponder]-aʒam`

Intended meaning:

"I often ponder the cause."

`cause` is a noun referring to the thing that leads to an effect, not a conjunction meaning "because."

## 8.6 Evaluating complexity

`Totemo, [electric-brain] Yagami [complex]-aʒam`

Intended meaning:

"I feel the Yagami program keeps getting more complicated."

The ingroup ending identifies the relevant evaluator or experiencer.

The comma makes `Totemo` a proposition-level modifier.

## 8.7 Difficulty with documentation

`So, kois totemos konpi faz-[difficult]-arm`

Intended meaning:

"So, I'm struggling to document all my ideas."

Important observations:

- `So` introduces a consequence or transition.
- `kois totemos` means "all ideas."
- `konpi faz` means writing nonfiction, or more generally producing nonfiction text.
- The perspective-oriented ending identifies the speaker as the one experiencing or evaluating the difficulty.

## 8.8 Immediate necessity

`Totemo, t'[try]-arm`

Intended meaning:

"I must keep trying."

`Totemo` supplies the recurring/continuing meaning.

`t'...-arm` supplies the pressing immediate necessity.

## 8.9 Evaluating the language

`Yagami [grammar]-[difficult]-arm`

Intended meaning:

"I find Yagami grammar difficult."

The predicate is interpreted through the ingroup perspective, rather than as an exclusively objective statement about the language.

## 8.10 Negative benefit

`bene-nə-am`

Intended meaning:

"This isn't beneficial to me/us."

The ingroup is the affected or relevant participant.

This contrasts with the perspective-oriented use of `-arm`.

## 8.11 Desire

`har-tai-am`

Intended meaning:

"I/we want [something to happen]."

The ingroup is associated with the desire.

This construction is an important precedent for preserving `-am` separately from `-arm`.

---

# 9. Unresolved or provisional areas

The following should not be treated as fully specified rules until further decisions are made.

1. Exact future vowel alternation across social-alignment endings.
2. Standalone first-person plural pronoun.
3. Equational copula rules.
4. Full details of the interaction between `t'` / `n'` and initial consonant mutation.
5. Whether initial consonant mutation will be avoided or conditioned by epenthesis.
6. Complete distribution and frequency of the nine spatial-social pronominal forms.
7. Further semantic suffixes and their individual meanings.
8. Full distribution of the `-am` versus `-arm` distinction across predicate classes.
9. Whether equivalent perspective-oriented constructions exist for the outgroup and socially distant alignments.
10. Whether the perspective distinction generalizes systematically across past and future tenses.
11. Exact morphological decomposition and historical development of `-arm`.
12. Full aspectual distribution of `-il`.
13. Exact rules for discourse-level modifier scope and ellipsis across multiple clauses.
14. Whether the different uses of `-r` as verbalizer and present-tense ending share a historical origin.

### Historical and grammatical hypotheses

The following are plausible interpretations, not established facts:

- `-am` may have developed from a broader ingroup-oriented relationship marking affectedness, involvement, or experiencer alignment.
- `-arm` may have developed through the addition or grammaticalization of a present-tense `-r` element, producing a distinct ingroup-perspective construction.
- The distinction may eventually generalize to other social alignments and tenses.

Do not generate hypothetical paradigms as though they are established.

For example, forms such as `-art`, `-ark`, `-irm`, and `-anrm` must not be assumed valid or productive without confirmation.

---

# 10. Important parsing principles

When interpreting Yagami:

1. Do not assume conventional English pronoun meanings exhaust the meaning of a form.
2. Distinguish physical distance from social alignment.
3. Treat social boundaries as contextual and elastic.
4. Do not assume number is encoded by the verb's social-alignment endings.
5. Distinguish demonstrative reference from possession.
6. Preserve the fixed five-slot verb order.
7. Interpret helpers in relation to their root.
8. Treat `t'` and `n'` as clitics outside the five-slot chain.
9. Treat hyphens and apostrophes as pronounced glottal-stop boundaries.
10. Distinguish productive compounds from lexicalized forms.
11. Treat roots as omnicategorical unless a derivational process establishes a particular function.
12. Distinguish `-am` from `-arm`.
13. Interpret `-am` in terms of ingroup involvement, association, or affectedness.
14. Interpret `-arm` in terms of ingroup perspective or standpoint.
15. Do not reduce perspective marking to subjective judgment alone.
16. Distinguish undergoer-oriented verbalization from agent-oriented `faz` constructions.
17. Pay attention to commas when determining whether an expression modifies a noun phrase or a proposition.
18. Distinguish `Totemo` from `totemos`.
19. Allow discourse context to carry recurring or continuing meaning across clauses.
20. Do not assume English negative-concord rules apply to Yagami.
21. Do not invent rules for unresolved areas.
22. When an utterance appears grammatically inconsistent, identify the problem and explain the uncertainty rather than silently repairing it.

---

# 11. Central principle

Yagami organizes reference around relationships—physical, social, and contextual—rather than treating grammatical person as the fundamental starting point.

Its verbal morphology can encode not only who is socially involved in a situation, but also whose experience, interests, or perspective are relevant.

Its compounds express relationships between concepts, while its discourse structure distinguishes proposition-level framing from ordinary phrase modification.

**Most importantly: interpret Yagami according to its own relational grammar. Do not flatten its distinctions into conventional English subject, object, tense, or pronoun categories.**