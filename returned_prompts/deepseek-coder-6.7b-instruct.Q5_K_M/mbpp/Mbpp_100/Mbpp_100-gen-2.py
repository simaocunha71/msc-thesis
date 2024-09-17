
def next_smallest_palindrome(num):
    num = num + 1
    while str(num) != str(num)[::-1]:
        num = num + 1
    return num


