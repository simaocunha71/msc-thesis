def test_three_equal(num1, num2, num3):
    count = 0
    if num1 == num2:
        count += 1
    if num2 == num3:
        count += 1
    if num1 == num3:
        count += 1
    return count