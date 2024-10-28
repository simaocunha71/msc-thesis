
def max_aggregate(my_list):
    max_sum = 0
    max_name = ''
    for name, score in my_list:
        if score > max_sum:
            max_sum = score
            max_name = name
    return (max_name, max_sum)
