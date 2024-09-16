```
def next_smallest_palindrome(n):
    str_n = str(n)
    length = len(str_n)
    # Reverse the string
    rev_str_n = str_n[::-1]
    # Check if the reverse string is a palindrome
    if rev_str_n == str_n:
        # If it is return the next integer
        return int(str_n) + 1
    else:
        # Otherwise find the first character that is not the same
        i = 0
        while i < length and str_n[i] == rev_str_n[i]:
            i += 1
        # Return the integer with that character changed
        return int(str_n[:i] + str_n[i+1:])
```
