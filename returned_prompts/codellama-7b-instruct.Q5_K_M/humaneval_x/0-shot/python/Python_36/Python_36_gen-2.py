
def fizz_buzz(n: int):
    return sum(int(str(i) in '7') for i in range(1, n, 11) if i % 13 == 0)
