"""
def digit_distance_nums(x,y):
    x_str = str(x)
    y_str = str(y)
    if len(x_str) != len(y_str):
        return 'The input numbers must be of equal length'
    digit_sum = 0
    for i in range(len(x_str)):
        digit_sum += abs(int(x_str[i]) - int(y_str[i]))
    return digit_sum

# assert digit_distance_nums(1,2) == 1
"""

