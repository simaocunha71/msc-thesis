def digit_distance_nums(num1, num2):
    return abs(sum(map(int,str(num1))) - sum(map(int,str(num2))))