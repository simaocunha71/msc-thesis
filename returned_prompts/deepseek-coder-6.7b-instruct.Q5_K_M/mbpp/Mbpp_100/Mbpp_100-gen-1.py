def next_smallest_palindrome(n):
    while True:
        n += 1
        if str(n) == str(n)[::-1]:
            return n

print(next_smallest_palindrome(99))

#2

