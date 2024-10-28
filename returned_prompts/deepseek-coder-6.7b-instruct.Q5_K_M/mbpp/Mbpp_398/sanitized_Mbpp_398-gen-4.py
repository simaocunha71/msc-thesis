def sum_of_digits(lst):
    sum_list = []
    for i in lst:
        sum = 0
        for j in str(i):
            sum += int(j)
        sum_list.append(sum)
    return sum_list