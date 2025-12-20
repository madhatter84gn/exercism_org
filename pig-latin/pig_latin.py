import re

# We define a pattern that captures:
# Group 'consonants': Optional leading consonants (handling the specific 'qu' and 'y' rules)
# Group 'base': The rest of the word
WORD_PATTERN = re.compile(
    r"""
    \b                                  # Start at a word boundary
    (?P<consonants>                     # Named group for consonants
        (?!xr|yt)                       # Negative lookahead: ignore 'xr' or 'yt' (they act as vowels)
        y?                              # Optional 'y' at the start
        (qu|[bcdfghjklmnpqrstvwxz])* # 'qu' or standard consonants
    )?                                  # This whole group is optional (for vowel-starting words)
    (?P<base>\w+)                       # The rest of the word
    \b                                  # End at word boundary
    """,
    re.VERBOSE,
)

# We define the replacement format: Base + Consonants + "ay"
PIG_LATIN_FORMAT = r"\g<base>\g<consonants>ay"


def translate(text: str) -> str:
    # re.sub iterates over the string for us!
    return WORD_PATTERN.sub(PIG_LATIN_FORMAT, text)
