def next_smallest_palindrome(n):
    while True:
        n += 1
        if str(n) == str(n)[::-1]:
            return n

print(next_smallest_palindrome(99))

#OUTPUT: 101

"""
Explanation:
The function takes an integer as input. It then starts a loop that will continue indefinitely. 
Inside the loop, the input number is incremented by 1. If the string representation of this new number is equal to its reverse, 
it means that the number is a palindrome, so the function returns this number.
"""
<jupyter_output>
101
<jupyter_text>
Problem 2
<jupyter_code>
