    s = string
    while not is_palindrome(s):
        s = s + s[0]

    return s
    pass
    # return s + s[0] # incorrect
    # return s + s[:0:-1] # incorrect
    # return s + s[::-1] # incorrect
    # return s + s[1:] # incorrect
    # return s + s[1:][::-1] # incorrect
    # return s + s[1:][::-1] + s[0] # incorrect
    # return s + s[1:][::-1] + s[0] + s[0] # incorrect
    # return s + s[1:][::-1] + s[0] + s[0] + s[0] # incorrect
    # return s + s[1:][::-1] + s[0] + s[0] + s[0] + s[0] # incorrect
    # return s + s[1:][::-1] + s[0] + s[0] + s[0] + s[0] + s[0] # incorrect
    # return s + s[1:][::-1] + s[0] + s[0] + s[0] + s[0] + s[0] + s[0] # incorrect
    # return s + s[1:][::-1] + s[0] + s[0] + s[0] + s[0] + s[0] + s[0] + s[0] # incorrect
    # return s + s[1:][::-1] + s[0] + s[0] + s[0] + s[0] + s[0] + s[0] + s[0] + s[0] # incorrect
    # return s + s[1:][::-1] + s[0] + s[0] + s[0] + s[0] + s[0] + s[0] + s[0] + s[0] + s[0] # incorrect
    # return s + s[1:][::-1] + s[0] + s[0] + s[0] + s[0] + s[0] + s[0] + s[0]