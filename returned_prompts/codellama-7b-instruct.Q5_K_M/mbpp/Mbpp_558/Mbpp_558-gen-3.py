
def digit_distance_nums(num1, num2):
    distance = 0
    while num1 > 0 or num2 > 0:
        distance += abs(num1 % 10 - num2 % 10)
        num1 //= 10
        num2 //= 10
    return distance


