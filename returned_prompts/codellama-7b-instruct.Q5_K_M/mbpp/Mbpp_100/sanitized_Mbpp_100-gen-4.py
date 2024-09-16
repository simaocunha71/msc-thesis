def next_smallest_palindrome(n):
    # 1. convert to string
    s = str(n)
    # 2. append the original string to the end of the string
    s = s + s[::-1]
    # 3. find the first number not equal to itself's reverse
    i = 0
    while i < len(s) and s[i] == s[~i]:
        i += 1
    # 4. increment the number
    return int(s[:i] + str(int(s[i]) + 1))