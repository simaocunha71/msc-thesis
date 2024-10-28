
def next_smallest_palindrome(num: int):
    if num % 2 == 0:
        return num + 1
    else:
        while True:
            if str(num + 1) == str(num + 1)[::-1]:
                return num + 1
            else:
                num += 2


