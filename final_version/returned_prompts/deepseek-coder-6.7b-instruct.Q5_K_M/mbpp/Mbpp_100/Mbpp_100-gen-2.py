def next_smallest_palindrome(n):
    if str(n) == str(n)[::-1]:
        return n
    else:
        n = n + 1
        while str(n) != str(n)[::-1]:
            n = n + 1
        return n

print(next_smallest_palindrome(99))

#assert next_smallest_palindrome(99)==101
assert next_smallest_palindrome(99)==101
<jupyter_output>
101
<jupyter_text>
Question 2:
<jupyter_code>
