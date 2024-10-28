    if n < 0:
        raise ValueError("Input should be a non-negative integer.")
    if n == 0 or n == 1:
        return 0
    if n == 2:
        return 2

    fib4_values = [0, 0, 2, 0]
    for i in range(4, n + 1):
        fib4_values.append(fib4_values[i - 1] + fib4_values[i - 2] + fib4_values[i - 3] + fib4_values[i - 4])

    return fib4_values[n]
    # or use a loop instead of list comprehension
    # result = 0
    # for i in range(4, n + 1):
    #     result = result + fib4_values[i - 1] + fib4_values[i - 2] + fib4_values[i - 3] + fib4_values[i - 4]
    #     fib4_values.append(result)  # or fib4_values[i] = result
    # return result


