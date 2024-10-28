
def hex_key(num):
    # check if the input is empty string
    if not num:
        return 0
    count = 0
    for digit in num:
        if digit in 'ABED':
            count += 1
    return count

The idea of the solution is to go through the string and check each digit
whether it is in the list of prime digits ('ABED'). If the digit is in the
list, increase the count by 1.
