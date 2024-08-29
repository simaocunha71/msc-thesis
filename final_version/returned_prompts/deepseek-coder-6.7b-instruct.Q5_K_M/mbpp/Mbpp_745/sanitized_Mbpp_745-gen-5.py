def divisible_by_digits(startnum, endnum):
    divisible_list = []
    for num in range(startnum, endnum+1):
        if num < 10:
            divisible_list.append(num)
        else:
            str_num = str(num)
            for digit in str_num:
                if num % int(digit) != 0:
                    break
            else:
                divisible_list.append(num)
    return divisible_list