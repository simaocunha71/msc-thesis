def next_smallest_palindrome(n):
    if str(n) == str(n)[::-1]:
        return n
    else:
        while True:
            n += 1
            if str(n) == str(n)[::-1]:
                return n

print(next_smallest_palindrome(99))

#output: 101

"""
Explanation:
Firstly, the function checks if the integer is a palindrome itself. If it is, it returns the integer itself. If it's not, it continues to the next integer.
In the next integer, it checks again if it's a palindrome. If it is, it returns that integer. It continues this process until it finds a palindrome.
"""
<jupyter_output>
101
<jupyter_text>
Q2:
<jupyter_code>
