

def fibfib(n: int):
    if n == 0 or n == 1:
        return 0
    elif n == 2:
        return 1

    fibfib_nums = [0, 0, 1]

    for i in range(3, n + 1):
        fibfib_nums.append(fibfib_nums[i - 1] + fibfib_nums[i - 2] + fibfib_nums[i - 3])

    return fibfib_nums[n]


print(fibfib(1))
print(fibfib(5))
print(fibfib(8))


