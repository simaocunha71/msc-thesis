def is_undulating(num):
    num_str = str(num)
    if len(num_str) == 1:
        return True
    first_num = int(num_str[0])
    second_num = int(num_str[1])
    for i in range(2, len(num_str)):
        if int(num_str[i]) >= first_num and int(num_str[i]) >= second_num:
            return False
        if i == len(num_str) - 1:
            break
        first_num = second_num
        second_num = int(num_str[i + 1])
    return True