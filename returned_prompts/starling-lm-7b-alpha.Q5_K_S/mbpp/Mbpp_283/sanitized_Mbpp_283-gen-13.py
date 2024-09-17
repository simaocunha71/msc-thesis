def validate(num):
    num_list = [int(i) for i in str(num)]
    for i in range(len(num_list)):
        if num_list[i] > num_list.count(num_list[i]):
            return False
    return True