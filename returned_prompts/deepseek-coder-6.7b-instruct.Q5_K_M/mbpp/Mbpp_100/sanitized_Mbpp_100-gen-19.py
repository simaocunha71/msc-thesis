def next_smallest_palindrome(num):
    while str(num) != str(num)[::-1]:
        num += 1
    return num