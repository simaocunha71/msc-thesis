def next_smallest_palindrome(num):
    if str(num) == str(num)[::-1]:
        num += 1
    while str(num) != str(num)[::-1]:
        num += 1
    return num


print(next_smallest_palindrome(99))  # 101

# Alternative Solution
def next_smallest_palindrome_alt(num):
    num += 1
    while str(num) != str(num)[::-1]:
        num += 1
    return num


print(next_smallest_palindrome_alt(99))  # 101

# Alternative Solution 2
def next_smallest_palindrome_alt2(num):
    while True:
        num += 1
        if str(num) == str(num)[::-1]:
            return num


print(next_smallest_palindrome_alt2(99))  # 101

# Alternative Solution 3
def next_smallest_palindrome_alt3(num):
    while True:
        num += 1
        if str(num) == str(num)[::-1]:
            return num
        if num > 9999999999:  # limit to prevent infinite loop
            return None


print(next_smallest_palindrome_alt3(99))  # 101

# Alternative Solution 4
def next_smallest_palindrome_alt4(num):
    num = int(str(num + 1))  # cast to int to ignore leading zero
    return num if str(num) == str(num)[::-1] else next_smallest_palindrome_alt4(num)


print(next_smallest_palindrome_alt4(99))  # 101

# Alternative Solution 5
def next_smallest_palindrome_alt5(num):
    def is_palindrome(n):
        return str(n) == str(n)[::-1]

    num += 1