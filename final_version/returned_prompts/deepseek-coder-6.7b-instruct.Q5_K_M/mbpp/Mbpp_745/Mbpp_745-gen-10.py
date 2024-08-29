def divisible_by_digits(startnum, endnum):
    divisible_by_digits_list = []
    for num in range(startnum, endnum + 1):
        if num < 10:
            divisible_by_digits_list.append(num)
        else:
            str_num = str(num)
            if '0' in str_num:
                continue
            else:
                digits = [int(i) for i in str_num]
                if all(num % digit == 0 for digit in digits):
                    divisible_by_digits_list.append(num)
    return divisible_by_digits_list

print(divisible_by_digits(1,22))

# Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]
<jupyter_output>
[1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]
<jupyter_text>
