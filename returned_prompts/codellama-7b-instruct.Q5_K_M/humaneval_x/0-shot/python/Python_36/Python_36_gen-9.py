
def fizz_buzz(n: int):
    count = 0
    for i in range(n):
        if i % 11 == 0 or i % 13 == 0:
            if str(i)[-1] == '7':
                count += 1
    return count
