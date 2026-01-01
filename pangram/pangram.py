import string


def is_pangram(sentence):
    cisentence = sentence.lower()
    found_letters = set()

    for char in cisentence:
        if "a" <= char <= "z":
            found_letters.add(char)

    return len(found_letters) == 26
