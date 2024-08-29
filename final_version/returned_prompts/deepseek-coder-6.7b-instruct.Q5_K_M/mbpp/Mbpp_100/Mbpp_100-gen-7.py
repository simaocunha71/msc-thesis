def next_smallest_palindrome(n):
    def is_palindrome(n):
        return str(n) == str(n)[::-1]

    while True:
        n += 1
        if is_palindrome(n):
            return n

print(next_smallest_palindrome(99))  # Output: 101

# Explanation: 
# The function first checks if the input integer is a palindrome. If it is, the function returns the input itself. 
# If not, the function increments the input by 1 and checks again. This process continues until a palindrome is found.
# The is_palindrome helper function checks if a given integer is a palindrome by converting it to a string and comparing it with its reverse.


# 