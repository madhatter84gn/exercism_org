import re

VOWELS = set("aeiou")


def translate(text: str) -> str:
    translated_words = []

    words = text.split(" ")
    for word in words:
        rule_number = get_rule_number(word)

        if rule_number == 1:
            translated_words.append(process_rule_1(word))

        if rule_number == 2:
            translated_words.append(process_rule_2(word))

        if rule_number == 3:
            translated_words.append(process_rule_3(word))

        if rule_number == 4:
            translated_words.append(process_rule_4(word))

    return " ".join(translated_words)


def get_rule_number(text: str) -> int:
    text = text.lower()

    if text[0] in VOWELS or text.startswith("xr") or text.startswith("yt"):
        return 1

    if re.match(r"^[^aeiou]*qu", text):
        return 3

    if re.match(r"^[^aeiou]+y", text):
        return 4

    if re.match(r"^[^aeiou]+", text):
        return 2

    return -1


def process_rule_1(text: str) -> str:
    return text + "ay"


def process_rule_2(text: str) -> str:
    # If a word begins with one or more consonants, first move those consonants to the end of the word and then add an `"ay"` sound to the end of the word.
    #
    # For example:
    #
    # - `"pig"` -> `"igp"` -> `"igpay"` (starts with single consonant)
    # - `"chair"` -> `"airch"` -> `"airchay"` (starts with multiple consonants)
    # - `"thrush"` -> `"ushthr"` -> `"ushthray"` (starts with multiple consonants)

    i = 0
    while i < len(text) and text[i].lower() not in VOWELS:
        i += 1
    return text[i:] + text[:i] + "ay"


def process_rule_3(text: str) -> str:
    m = re.match(r"^([^aeiou]*qu)(.+)", text.lower())
    if not m:
        return process_rule_2(text)  # defensive fallback

    prefix = m.group(1)  # like "qu" or "squ" or "thrqu" (if that existed)
    rest = text[len(prefix) :]  # keep original casing slicing if you care later
    return rest + text[: len(prefix)] + "ay"


def process_rule_4(text: str) -> str:
    for i, ch in enumerate(text):
        if ch == "y" and i > 0:
            return text[i:] + text[:i] + "ay"

        if ch in VOWELS:
            break  # real vowel found first → not rule 4

    return text


if __name__ == "__main__":
    result = translate("quick fast run")
    print(result)
