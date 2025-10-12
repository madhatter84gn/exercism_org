def equilateral(sides):
    if not check_validity(sides):
        return False

    a, b, c = sorted(sides)
    return a == c


def isosceles(sides):
    if not check_validity(sides):
        return False

    a, b, c = sorted(sides)
    return a == b or b == c


def scalene(sides):
    if not check_validity(sides):
        return False

    a, b, c = sorted(sides)
    return a != b and b != c and a != c


def check_validity(sides):
    a, b, c = sorted(sides)
    return a > 0 and a + b > c
