"""
def next_smallest_palindrome(n):
    if n < 10:
        return n+1
    x = str(n)
    if x[::-1] == x:
        return n+1
    p = x[0]
    for i in range(len(x)-1, 0, -1):
        if x[i] != p:
            break
        p = x[i]
    if p == '9':
        return int(x[:i-1] + '0' + x[i:])
    else:
        return int(x[:i] + chr(ord(x[i])+1) + x[i+1:])

def next_smallest_palindrome(n):
    while True:
        s = str(n)
        if s == s[::-1]:
            return n
        n += 1

def next_smallest_palindrome(n):
    s = str(n)
    if s == s[::-1]:
        return n
    l = len(s)
    for i in range(l):
        if s[i] != '9':
            break
    s = s[:i] + chr(ord(s[i])+1) + s[i+1:]
    return int(s)
"""

def next_smallest_palindrome(n):
    while True:
        s = str(n)
        if s == s[::-1]:
            return n
        n += 1

def next_smallest_palindrome(n):
    s = str(n)
    if s == s[::-1]:
        return n
    l = len(s)
    for i in range(l):
        if s[i] != '9':
            break
    s = s[:i] + chr(ord(s[i])+1) + s[i+1:]
    return int(s)

def next_smallest_palindrome(n):
    while True:
        s = str(n)
        if s == s[::-1]:
            return n
