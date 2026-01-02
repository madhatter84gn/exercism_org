import string


def is_isogram(input: str) -> bool:
    letters = "".join(char for char in input.lower() if char in string.ascii_lowercase)
    return len(letters) == len(set(letters))
