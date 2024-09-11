def is_Harshad(num):
    temp = num
    sum = 0
    while temp > 0:
        digit = temp % 10
        sum += digit
        temp //= 10
    if sum % num == 0:
        return True
    else:
        return False

# Test
assert is_Harshad(153) == True



"""
Write a Python function