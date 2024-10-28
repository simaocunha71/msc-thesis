    count = 0
    for num in nums:
        if num > 10:
            if str(num)[0] == '1' or str(num)[0] == '3' or str(num)[0] == '5' or str(num)[0] == '7' or str(num)[0] == '9':
                if str(num)[-1] == '1' or str(num)[-1] == '3' or str(num)[-1] == '5' or str(num)[-1] == '7' or str(num)[-1] == '9':
                    count += 1

    return count


