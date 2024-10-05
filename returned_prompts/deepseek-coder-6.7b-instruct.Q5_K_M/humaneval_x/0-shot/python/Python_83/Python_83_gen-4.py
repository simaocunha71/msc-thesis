
    count = 0

    # loop through all n-digit numbers
    for i in range(10**(n-1), 10**n):

        # convert number to string for easy access to digits
        str_i = str(i)

        # increment count if number starts or ends with 1
        if str_i[0] == '1' or str_i[-1] == '1':
            count += 1

    return count

# test
print(starts_one_ends(2))  # should return 10 (12, 13, 14, 15, 16, 17, 18, 19, 21)
print(starts_one_ends(3))  # should return 20
print(starts_one_ends(4))  # should return 30
print(starts_one_ends(1))  # should return 1 (only 1-digit number that starts or ends with 1)

