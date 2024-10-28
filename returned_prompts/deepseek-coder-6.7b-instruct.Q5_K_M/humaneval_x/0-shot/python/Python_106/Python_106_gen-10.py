
def f(n):
    def fact(num):
        if num == 0:
            return 1
        else:
            return num * fact(num - 1)

    def sum_num(num):
        if num == 0:
            return 0
        else:
            return num + sum_num(num - 1)

    return [fact(i) if i % 2 == 0 else sum_num(i) for i in range(1, n + 1)]


print(f(5))  # [1, 2, 6, 24, 15]

# 2.

