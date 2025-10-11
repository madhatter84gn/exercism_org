def is_armstrong_number(number: int) -> bool:
    digits = [int(digit) for digit in str(number)]
    number_of_digits = len(digits)

    total = 0
    for d in digits:
        total += d**number_of_digits

    return total == number
