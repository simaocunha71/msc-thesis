
def hex_key(num):
    """
    Prime numbers are 2, 3, 5, 7, 11, 13, 17,...
    """
    prime_list = [2,3,5,7,11,13,17]
    count = 0
    if num == '':
        return 0
    for i in range(len(num)):
        if num[i] in 'ABED':
            count += 1
    for i in range(len(num)):
        if num[i] in prime_list:
            count += 1
    return count

