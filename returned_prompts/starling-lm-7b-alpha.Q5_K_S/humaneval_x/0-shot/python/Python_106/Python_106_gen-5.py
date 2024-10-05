
def f(n):
    if n == 1:
        return [1]
    else:
        res = []
        for i in range(1, n + 1):
            if i % 2 == 0:
                res.append(fact(i))
            else:
                res.append(sum(range(1, i + 1)))
        return res


def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n - 1)


def sum(n):
    if n == 0:
        return 0
    else:
        return n + sum(n - 1)


# print(f(5))
# print(f(6))


# My Solution
def f(n):
    if n == 1:
        return [1]
    else:
        res = []
        for i in range(1, n + 1):
            if i % 2 == 0:
                res.append(fact(i))
            else:
                res.append(sum(i))
        return res


def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n - 1)


def sum(n):
    if n == 0:
        return 0
    else:
        return n + sum(n - 1)


print(f(5))
print(f(6))

# My Solution
def f(n):
    if n == 1:
        return [1]
    else:
        res = []
        for i in range(1, n + 1):
            if i % 2 == 0:
                res.append(fact(i))
            else:
                res.append(sum(i))
        return res


def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n - 1)


def sum(n):
    if n == 0:
        return 0
   