DROPS = ("i", 3), ("a", 5), ("o", 7)


def convert(number: int) -> str:
    return "".join(f"Pl{i}ng" for i, v in DROPS if not number % v) or str(number)
