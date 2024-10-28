
def fib4(n: int):
    result = 0
    for i in range(n):
        result = result + fib4(i)
    return result


