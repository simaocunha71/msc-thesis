def digit_distance_nums(n1, n2):
    n1 = str(n1)
    n2 = str(n2)
    if len(n1) != len(n2):
        return "Incorrect input"
    sum_of_distance = 0
    for i in range(len(n1)):
        sum_of_distance += abs(int(n1[i]) - int(n2[i]))
    return sum_of_distance