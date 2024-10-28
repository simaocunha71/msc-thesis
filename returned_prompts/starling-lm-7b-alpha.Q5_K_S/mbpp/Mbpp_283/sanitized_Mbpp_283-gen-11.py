def validate(num):
    num_str = str(num)
    num_list = [int(x) for x in num_str]

    for i in range(len(num_list)):
        if num_list[i] > num_list.count(num_list[i]):
            return False
    return True