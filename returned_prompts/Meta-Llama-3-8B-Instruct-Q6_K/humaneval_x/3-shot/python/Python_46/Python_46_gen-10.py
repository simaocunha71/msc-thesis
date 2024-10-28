    if n < 4:
        return [0, 0, 2][n]
    fib4_list = [0, 0, 2, 0]
    for i in range(4, n):
        fib4_list.append(fib4_list[i-1] + fib4_list[i-2] + fib4_list[i-3] + fib4_list[i-4])
    return fib4_list[n-1]  # fib4_list is 0-indexed, so n-1 is the correct index


