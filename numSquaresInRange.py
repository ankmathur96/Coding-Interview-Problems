def num_squares(lower, upper):
    result = 0
    current, square = 0, 0
    while square < lower:
        current += 1
        square = current ** 2
    while square < upper:
        result += 1
        current += 1
        square = current ** 2
    if square == upper:
        result += 1
    return result