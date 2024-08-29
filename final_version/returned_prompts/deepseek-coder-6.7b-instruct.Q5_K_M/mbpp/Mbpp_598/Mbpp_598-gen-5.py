def armstrong_number(num):
    num_list = [int(x) for x in str(num)]
    return num == sum([x**len(num_list) for x in num_list])

assert armstrong_number(153) == True
"""
