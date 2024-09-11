def test_three_equal(num1, num2, num3):
    counter = 0
    if num1 == num2:
        counter += 1
    if num2 == num3:
        counter += 1
    if num1 == num3:
        counter += 1
    return counter