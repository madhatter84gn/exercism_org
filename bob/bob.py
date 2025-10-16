def response(hey_bob: str) -> str:
    is_question = is_input_a_question(hey_bob)
    is_shouting = is_input_shouting(hey_bob)
    is_silent_or_whitespace = is_input_silent(hey_bob)

    if is_shouting and is_question:
        return "Calm down, I know what I'm doing!"

    if is_question:
        return "Sure."

    if is_shouting:
        return "Whoa, chill out!"

    if is_silent_or_whitespace:
        return "Fine. Be that way!"

    return "Whatever."


def is_input_silent(input: str) -> bool:
    return not input.strip()


def is_input_shouting(input: str) -> bool:
    return input.isupper()


def is_input_a_question(input: str) -> bool:
    return input.strip().endswith("?")
