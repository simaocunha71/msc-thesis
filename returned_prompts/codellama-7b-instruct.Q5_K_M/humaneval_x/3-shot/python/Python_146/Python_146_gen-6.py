    count = 0

    for num in nums:
        if num > 10:
            num_str = str(num)
            if num_str[0] == '1' or num_str[0] == '3' or num_str[0] == '5' or num_str[0] == '7' or num_str[0] == '9':
                if num_str[-1] == '1' or num_str[-1] == '3' or num_str[-1] == '5' or num_str[-1] == '7' or num_str[-1] == '9':
                    count += 1

    return count


