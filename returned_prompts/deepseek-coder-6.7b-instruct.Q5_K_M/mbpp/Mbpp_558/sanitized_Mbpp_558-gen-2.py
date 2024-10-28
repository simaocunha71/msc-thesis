def digit_distance_nums(num1, num2):
    return sum(abs(int(a)-int(b)) for a, b in zip(str(num1), str(num2)))