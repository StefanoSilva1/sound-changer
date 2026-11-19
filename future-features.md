Conlang Creator: Technical Specification & Implementation Roadmap

Project Summary

**Conlang Creator** is a Python-based computational linguistics suite designed to manage the full lifecycle of a deep-time constructed language—from minimalist proto-roots (EOPX → MOPX → LOPX) through complex phonological evolution (PK → K) and historical orthography.

Unlike basic regex replacers, the engine is **phonologically aware**: it understands articulatory IPA features, multi-character phonemes, stress, and morphological boundaries. The system is organized into four implementation phases:

1. **Phonological Knowledge Base & Era Profiles:** A built-in articulatory IPA matrix, smart multi-character tokenizer, and customizable per-era alphabet/feature tables.  
2. **Phonological & Orthographic Rule Engine:** A custom rule parser supporting variables, paired change groups, wildcards, exceptions, directional vowel harmony, and context-sensitive IPA-to-orthography mapping.  
3. **Lexicon Workflow & UI Tools:** Live rule previews, simultaneous/sequential execution toggles, an interactive IPA symbol picker, and UTF-8 LingoCon CSV import/export with automated etymology changelogs.  
4. **Future Interactive Writing Tools:** An automated Compound Builder and a Japanese-IME-style Dual-Mode Glossing Editor that inflects words on the fly across any historical stage.  
   ---

Phase 1: Phonological Foundation & Data Model

1\. Built-In IPA Chart & Feature Matrix

The engine natively maps every IPA character to its articulatory coordinates and natural classes so rules can target sounds by feature rather than raw character lists:

* **Consonant Coordinates:** Manner (plosive, nasal, fricative, affricate, approximant, trill, tap), Place (bilabial, labiodental, dental, alveolar, postalveolar, retroflex, palatal, velar, uvular, glottal), and Phonation (voiced, voiceless).  
* **Vowel Coordinates:** Height (close, near-close, close-mid, mid, open-mid, near-open, open), Backness (front, central, back), and Rounding (rounded, unrounded).  
* **Natural Class Nicknames:** Supports shorthand class selectors such as \[sonorant\], \[obstruent\], \[stop\], \[sibilant\], \[liquid\], \[glide\], and \[labial\].

**Use Existing Python Libraries for Heavy Lifting:** Libraries like **panphon** (which already maps every IPA symbol to articulatory features) and **rapidfuzz** (for instant fuzzy gloss search in your IME dropdown) can save you 3–4 weekends of manual data entry and search math.

2\. Input Parsing & Symbol Normalization

* **Case Folding:** Recognizes both uppercase and lowercase IPA inputs (e.g., B, G, R, N) and normalizes all standard output strictly to lowercase IPA symbols (reserving uppercase letters A–Z exclusively for Group variables in rule syntax).  
* **Interchangeable Delimiters:** Accepts commas (,) and forward slashes (/) interchangeably across all lists, group definitions, and inline sets.  
* **Dynamic Category Reassignment:** Allows any segment to be reclassified between Vowel (V) and Consonant (C) per era or preset (e.g., treating /w/ or /j/ as a vowel nucleus in one stage and a consonant onset in another).  
* **Diacritic & Transcription Toggles:**  
  * **Diacritic Sensitivity:** Enable or disable diacritic discrimination per rule block.  
  * **Broad vs. Narrow Transcription:** Toggle between collapsing allophonic variants (e.g., treating ʀ and r as equivalent in Broad mode) and treating every IPA symbol as strictly distinct (Narrow mode).

3\. Specialized Phonetic Notation Handling

The tokenizer and renderer must parse and output the following specialized notations as unified phoneme tokens without splitting multi-character sequences:

| Phonetic Feature | Accepted Input Variants | Configurable Output Modes |
| ----- | ----- | ----- |
| **Long Vowels** | Triangular colon (aː), ASCII colon (a:), macron (ā) | Standard IPA (aː), Macron (ā), or Colon (a:) |
| **Glottal Stop** | IPA symbol (ʔ), straight apostrophe ('), question mark (?), morpheme hyphen (\- when configured) | Standard IPA (ʔ), Apostrophe ('), or Question mark (?) |
| **Ejectives** | Modifier letter apostrophe (pʼ, tʼ, kʼ), straight single apostrophe (p', t', k') | Standard IPA (pʼ) or Straight apostrophe (p') |
| **Aspiration & Secondary Articulation** | Superscript modifiers (bʰ, ɡʷ, ɡʷʰ, ɡʲ, ɡʲʰ) **or** flat digraphs (bh, gw, gwh, gj, gjh) | Toggleable between **Superscript Mode** (ɡʷ) and **Flat Digraph Mode** (gw) |
| **Syllabic Sonorants** | Combining ring below (r̥, l̥, m̥, n̥) or dedicated syllabic markers (n̩, l̩) | Preserves syllabic diacritics as single-unit V nuclei |
| **Laryngeal Theory** | Subscripted laryngeals (h₁, h₂, h₃) and flat equivalents (h1, h2, h3) | Standard subscript (h₁, h₂, h₃) or Flat (h1, h2, h3) |

4\. Per-Era Alphabet & Inventory Profiles

Because each historical stage (MOPX, LOPX, LNK, etc.) has its own active inventory and writing conventions, each language version stores a reusable profile:

| Column | Purpose | Examples |
| ----- | ----- | ----- |
| **Grapheme / Symbol** | The literal character, digraph, or IPA symbol allowed in that stage's words. | \<a\>, \<jə\>, \<sh\>, \<w\>, ʔ |
| **IPA Value** | The default spoken phoneme represented by that symbol. | /a/, /jə/, /ʃ/, /w/, /ʔ/ |
| **Primary Class** | Core phonological category (V for Vowel, C for Consonant, or Other). | V, C, Other |
| **Custom \[Feature\] Tags** | Arbitrary user-defined labels targetable directly in rules via \[feature\] syntax. | \[glide\], \[liquid\], \[silent\], \[palatal\], \[morpheme\_break\] |

* **Saved Settings & Rule Presets:** Users can save custom settings (digraph interpretations, output symbol preferences, V/C definitions, stress rules, and named rule sets) to reusable profile files and chain named rule sets in a custom execution order.  
  ---

Phase 2: Rule Syntax & Sound Change Engine

5\. Notation Conventions & Mode Headers

* **Linguistic Bracketing Standard:** Angle brackets \<...\> denote written orthography/letters (e.g., \<ph\>), while forward slashes /.../ denote spoken phonetic/phonemic sounds (e.g., /f/ or /v/).  
* **Dynamic Mode Headers:**  
  * When editing or running IPA rules, the UI header and rule-block tag display **/sound change/**.  
  * When editing or running spelling/Anglicization rules, the UI header and rule-block tag display **\<orthographic change\>**.  
* **Link / Unlink Toggle:**  
  * **Linked Mode (Early Eras):** Changes applied to /sound change/ automatically synchronize with \<orthographic change\>.  
  * **Unlinked Mode (Historical Divergence):** Spoken /sound change/ passes evolve the IPA column independently while \<orthographic change\> passes evolve the Lemma (spelling) column—allowing spellings to freeze and produce silent letters.

6\. Phoneme Groups & Change Groups

* **Standard Phoneme Groups:** Assigned on a single line using Name \= {elements} where Name is strictly a single uppercase letter (A–Z). Commas , and slashes / are interchangeable, and spaces are ignored (G \= {s, dh, rth} or G \= {s/dh/rth}). V and C are built-in default groups loaded from the active era profile.  
* **Change Groups (Paired Mappings):** Marked with an asterisk (\*) during assignment (Name\* \= {source \> target; ...}) to define one-to-one shifts:  
  * Supports nested local environments and exceptions inside the braces:  
    text

```
B* = {b > p; d > t / #_; d > th // #_; g > k}
```

  *   
    Use code with caution.  
  * When Name appears in both Target and Result (VB \-\> VB), each matched source swaps for its mapped partner. If a conditional sub-rule does not match, the segment remains unchanged.

7\. Rule Anatomy & Operators

Every rule follows up to four components:

text

```
Target -> Result / Environment // Exception /// Stop
```

Use code with caution.

| Component | Operator | Required? | Function |
| ----- | ----- | ----- | ----- |
| **Change** | \-\> (also ➙ or \>) | **Yes** | Defines Target and Result. Applies unconditionally if alone. |
| **Environment** | / | No | Restricts the change to a specific context around \_. |
| **Exception** | // | No | Blocks the change if the context matches this pattern. |
| **Stop (Until)** | /// | No | Halts directional propagation (\< or \>) when a blocker is hit. |

8\. The Change Field (Target \-\> Result)

* **Deletion:** Use ∅ (or omit in multi-part replacements) to delete a matched sound.  
* **Group Preservation (Same Group):** If a group appears in both Target and Result (VG \-\> VtG), the matched phoneme remains unchanged (as → ats).  
* **Random Selection (Different Group):** If a *new* standard group appears in the Result (VG \-\> VB), the engine selects a random member from B (as → ak, ag, or ab).  
* **Wildcard Backreferences:** Wildcards (\*) in the Target mirror into the Result to preserve inner characters while modifying outer ones:  
  text

```
o*e -> ə*∅ / _ne#   (or: o*e -> ə* / _Ce#)
```

*   
  Use code with caution.  
  *(Matches done → dən, preserving n while changing o → ə and deleting e → ∅.)*

9\. Environment (/) & Exception (//) Syntax

* **Position & Boundaries:** \_ marks the target's slot (a \-\> e / t\_, ar \-\> et / l\_l, a \-\> e / V\_). \# marks a word boundary (\#\_ word-initial, \_\# word-final).  
* **Standalone & Stacked Exceptions:** // can be used alone (a \-\> e // \_\#) or stacked after an environment (a \-\> e / \#\_ // \_s). Multiple environments or exceptions can be separated by commas.  
* **Wildcards & Optional Elements:**

| Syntax | Meaning | Example Pattern | Matches | Does Not Match |
| ----- | ----- | ----- | ----- | ----- |
| **\*** | Exactly **1** arbitrary phoneme | o(\*)e | oe, ode | odde |
| **\*\*** | **1 or more** arbitrary phonemes | dr\*\*n | drawn, drain, drone | drn |
| **G** | Group acts as a **constrained 1-unit wildcard** | oBe *(where B={k,g,b})* | oke, oge, obe | oe, okbe |
| **(...)** | **Optional** sequence (0 or 1 occurrence) | o(d)e | oe, ode | odde |
| **(G)** | Optional group member | o(B)e | oe, oke, oge, obe | okbe |
| **(GG)** | Optional pair of group members | o(BB)e | oe, okbe, ogke | oke *(only 1 B)* |
| **(G)b** | Optional G followed by required b | o(B)be | obe, okbe, ogbe, obbe | oe *(missing b)* |

10\. Directional Propagation (\<, \>), Features, & Stop (///)

Used for iterative spreading rules such as vowel harmony or long-distance assimilation:

* **Feature Labels (\[label\]):** Shifts a target along an articulatory feature (V \-\> \[front\]). Segments already possessing that feature remain unchanged.  
* **Directional Operators:** \< spreads right-to-left (regressive: V \-\> \[front\] / \< i), and \> spreads left-to-right (progressive: V \-\> \[round\] / u \>).  
* **Inline Groups ({...}):** Ad-hoc trigger or blocker sets written inside braces (V \-\> \[front\] / \< {i, y, e}).  
* **Opaque Stop (///) vs. Transparent Exception (//):**  
  * V \-\> \[front\] / \< i // s\_ /// e  
  * During propagation, matching an **Exception (// s\_)** skips that single vowel without stopping the wave; hitting a **Stop (/// e)** or word boundary (\#) terminates propagation immediately for the rest of the word.

11\. Contextual IPA-to-Orthography Mapping (IPA \-\> \<Spelling\>)

Each era profile includes an ordered **Orthographic Representation Panel** that uses the exact same rule syntax to map spoken IPA into context-sensitive spelling from top (most specific) to bottom (general fallback):

text

```
/k/  -> <c>   / _ {a, o, u}
/k/  -> <k>   / _ {e, i}
/k/  -> <ck>  / V[short]_#
/tʃ/ -> <tch> / V[short]_#
/tʃ/ -> <ch>  // V[short]_#
```

Use code with caution.  
---

Phase 3: Execution Controls, UI, & LingoCon Workflow

12\. Rule Execution & Live Preview

* **Preview Toggle:** Toggleable live preview pane showing before-and-after word transformations before committing changes to the lexicon.  
* **Simultaneous vs. Sequential Toggle:** Switchable execution mode allowing a rule block to evaluate all rules against the original input snapshot simultaneously, or cascade sequentially one rule after another.  
* **Stress Rules:** Configurable stress assignment pass (initial, penultimate, weight-sensitive, or lexical ˈ / ˌ) that can feed into downstream vowel reduction or lengthening.

13\. LingoCon CSV Interoperability & Etymology Changelog

* **LingoCon CSV Support:** Reads and writes standard UTF-8 LingoCon CSV exports (Lemma,Gloss,IPA,Part of Speech,Etymology,Notes,Tags,Related Words) preserving all columns and diacritics.  
* **Etymology Changelog Popup:** When committing a batch of changes, a dialog prompts for the outgoing **Stage / Language Name** (e.g., entering "MOPX" appends \> MOPX \[old\_form\] gloss to modified entries). Includes a **Silent** option to apply fixes or test passes without updating the Etymology column, and automatically skips unchanged words.

14\. Interactive IPA Symbol Picker

* **Clickable IPA Grid:** Interactive consonant and vowel chart that inserts clicked symbols directly into the active input or rule editor.  
* **Visual & Acoustic Search:** Typing a Latin character (e.g., r) filters the picker to show visually and acoustically related IPA symbols (r, ɾ, ɽ, ɹ, ɻ, ʀ, ʁ).  
* **Paired Variant Display:** Selecting or hovering over any symbol displays its **uppercase rule-variable equivalent** and its **voiced / voiceless counterpart** (e.g., /s/ ↔ /z/, /r/ ↔ /r̥/).  
  ---

Phase 4: (Later) Interactive Writing & Coinage Tools

15\. Interactive Compound Builder Pipeline

When selecting two or more roots in search fields (e.g., **pi** *look/attention* and **kju** *come*), the tool automates coinage in four steps:

1. **Concatenate Raw Roots:** Joins the selected stems (pi \+ kju → \*pikju).  
2. **Apply Active Sound Changes:** Runs the current era's rule pass (k \> g / V\_V → **pigju**).  
3. **Generate IPA:** Tokenizes the evolved lemma via longest-match (\["p", "i", "g", "ju"\]) and populates the IPA field (pigju).  
4. **Prefill Etymology & Related Words:** Extracts primary glosses to prefill Etymology (MOPX \[pi\] look \+ \[kju\] come) and Related Words (pi; kju) in editable fields.  
* **Smart UX Features:** Includes a per-slot toggle to select either the **current Lemma** (pə) or an **underlying/earlier root** (pa), plus an **\+ button** to add 3rd/4th root slots.

16\. Dual-Mode IME Glossing & Translation Editor

An inline writing editor that lets you type either remembered conlang words or English glosses interchangeably:

* **Japanese-IME Style Candidate Menu:** Typing any word keeps it underlined as an active conversion buffer and opens a candidate window beneath the cursor searching both Lemma and Gloss / Gloss\_Key (with fuzzy matching). Cycle candidates with Space or Arrow Keys (or number keys) and press Enter to commit.  
* **Morphological Assembly & Inflection:** Attaching bound affixes with hyphens (e.g., tə-FUT or sleep-ana) joins stem and affix before running active sound changes (tə \+ \-ana → **tʌʔana** via ə \> ʌ and glottal hiatus \- → ʔ).  
* **Stacked Interlinear Output:** Commits the finished conlang surface form on the primary top line with aligned gloss tags directly underneath:  
  text

```
mi      pimju     piʔi
1SG     flower    look-PST
```

*   
  Use code with caution.  
* **Smart UX Features:** Supports seamless mixed-language input (mi flower look-PST) and includes an inline **\+ Coin Compound** option at the bottom of empty candidate lists to launch the Compound Builder mid-sentence and insert the new word upon saving.  
* **Use Existing Python Libraries for Heavy Lifting:** Libraries like **panphon** (which already maps every IPA symbol to articulatory features) and **rapidfuzz** (for instant fuzzy gloss search in your IME dropdown) can save you 3–4 weekends of manual data entry and search math.  
* 

# 