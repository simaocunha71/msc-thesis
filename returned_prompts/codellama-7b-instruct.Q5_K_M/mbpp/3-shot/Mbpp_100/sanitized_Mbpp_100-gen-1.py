def next_smallest_palindrome(num: int) -> int:
    if num == 0:
        return 1
    str_num = str(num)
    len_str_num = len(str_num)
    middle = len_str_num // 2
    if len_str_num % 2 == 0:
        if str_num[:middle] == str_num[:(len_str_num - 1) - middle]:
            return num + 1
        else:
            return num + 10
    else:
        if str_num[:middle] == str_num[(len_str_num - 1) - middle:]:
            return num + 1
        else:
            return num + 10