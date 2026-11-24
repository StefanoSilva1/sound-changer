# # Phonotactic Toolkit

# A configurable tool for generating, validating, and eventually linting syllables and words according to linguistic phonotactic rules.

# ## Architecture

# - **Language profiles:** Define each language's phoneme inventory, syllable structures, legal sound combinations, contextual restrictions, and other phonotactic rules.
# - **Approximation profiles:** Define substitutions, exclusions, and pronunciation preferences for adapting linguistic sounds to a user's needs. These must not alter the original language profiles.
# - **Rule sets:** Define how multiple profiles interact through set operations, including union (OR), intersection (AND), and difference (NOT). Users can save and reuse combinations.

# ## Core Requirements

# - Model actual linguistic phonology and phonotactics rather than relying on unrestricted lists of sounds and clusters.
# - Support contextual rules and dependencies between onsets, nuclei, codas, and adjacent syllables.
# - Support both single-language and mixed-language word generation.
# - Track which profiles license each generated or validated structure.
# - Allow users to enable, disable, combine, and upload profiles.
# - Preserve the ability to explain why a particular structure is permitted or rejected.

# ## Development Goals

# 1. Build a reliable syllable generator.
# 2. Expand it into a complete word generator.
# 3. Implement word validation against selected rule sets.
# 4. Develop a linter that identifies violations, unusual structures, and possible corrections.

# The linguistic rules, profile definitions, rule-set operations, and user interface should remain modular so they can be expanded independently.