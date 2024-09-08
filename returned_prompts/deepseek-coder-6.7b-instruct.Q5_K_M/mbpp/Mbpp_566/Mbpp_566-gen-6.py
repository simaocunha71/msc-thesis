
def sum_digits(n):
    #convert the number to a string
    n = str(n)
    #initialize the sum to 0
    sum = 0
    #iterate over each character in the string
    for digit in n:
        #convert the character back to an integer and add it to the sum
        sum += int(digit)
    #return the sum
    return sum

print(sum_digits(345))  # Output: 12


