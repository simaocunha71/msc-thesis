def next_smallest_palindrome(n):
    while True:
        n += 1
        if str(n) == str(n)[::-1]:
            return n


print(next_smallest_palindrome(99))  # Output: 101


"""
The function works by incrementing the input integer by 1, checking if the new number is a palindrome, and returning that number if it is. The loop continues until a palindrome is found. 

In the case of the input 99, the function starts by incrementing 99 to 100. 100 is not a palindrome, so it increments 100 to 101 and checks if 101 is a palindrome. It is, so the function returns 101.
"""

"""
