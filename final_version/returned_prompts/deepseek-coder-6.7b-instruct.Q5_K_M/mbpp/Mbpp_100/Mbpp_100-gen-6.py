
def next_smallest_palindrome(n):
    def is_palindrome(n):
        return str(n) == str(n)[::-1]

    n = n + 1
    while not is_palindrome(n):
        n = n + 1
    return n

print(next_smallest_palindrome(99))
<jupyter_output>
101
<jupyter_text>
Exercise 3:  Create a function that returns the number of elements that are smaller than the average of a list.
<jupyter_code>
