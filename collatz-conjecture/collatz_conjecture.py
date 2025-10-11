def steps(number: int) -> int:
    if number < 1:
        raise ValueError("Only positive integers are allowed")
    step_count = 0
    while number != 1:
        step_count += 1
        if number % 2 == 0:
            number = int(number / 2)
        else:
            print("ODD: ", number)
            number = (number * 3) + 1
    return step_count
