
def next_smallest_palindrome(num: int) -> int:
    num += 1
    while not is_palindrome(num):
        num += 1
    return num

def is_palindrome(num: int):
    return str(num) == str(num)[::-1]


