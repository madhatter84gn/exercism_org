def convert(number: int) -> str:
    results = []
    is_div_by_three = number % 3 == 0
    is_div_by_five = number % 5 == 0
    is_div_by_seven = number % 7 == 0

    if is_div_by_three:
        results.append("Pling")

    if is_div_by_five:
        results.append("Plang")

    if is_div_by_seven:
        results.append("Plong")

    if len(results) < 1:
        return str(number)

    return "".join(results)
