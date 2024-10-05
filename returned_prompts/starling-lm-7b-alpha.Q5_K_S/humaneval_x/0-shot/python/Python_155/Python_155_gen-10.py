
def even_odd_count(num):
    count_odd = 0
    count_even = 0
    num = abs(num)
    while num > 0:
        if num % 2 == 0:
            count_even += 1
        else:
            count_odd += 1
        num = num // 10
    return count_odd, count_even


# test cases
print(even_odd_count(-12)) # (1, 1)
print(even_odd_count(123)) # (1, 2)
print(even_odd_count(112)) # (2, 1)
print(even_odd_count(111)) # (1, 3)



# Python program to count number of even and
# odd digits in a number

def count_even_odd(n):
    # Initialize count for even and odd
    # digits to 0
    e = 0
    o = 0

    # Traverse the given number
    while (n != 0):
        # If last digit is even, e is
        # incremented by 1
        if (n % 10 % 2 == 0):
            e += 1
        # If last digit is odd, o is
        # incremented by 1
        else:
            o += 1

        # Removing last digit from number
        # variable n
        n = n / 10

    # Print the counts of even and odd
    # digits
    print("Number of even digits:", e)
    print("Number of odd digits:", o)

# Driver Code
num = -12
count_even_odd(num)





































































































