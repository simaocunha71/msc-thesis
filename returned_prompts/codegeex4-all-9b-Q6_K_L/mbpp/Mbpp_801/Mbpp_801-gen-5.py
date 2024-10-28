def test_three_equal(num1: int, num2: int, num3: int):
    if num1 == num2 == num3:
        return 3
    elif num1 == num2 or num1 == num3 or num2 == num3:
        return 2
    else:
        return 0

