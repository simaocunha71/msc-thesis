def armstrong_number(num):
    '''
    function to check whether the given number is armstrong or not
    '''
    num_str = str(num)
    num_len = len(num_str)
    sum = 0
    for i in range(num_len):
        sum += int(num_str[i]) ** num_len
    if sum == num:
        return True
    else:
        return False