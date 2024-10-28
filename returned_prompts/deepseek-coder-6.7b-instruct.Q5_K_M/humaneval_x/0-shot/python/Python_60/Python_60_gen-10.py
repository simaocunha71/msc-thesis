

def sum_to_n(n: int):
    return sum(range(1, n+1))


if __name__ == "__main__":
    import doctest
    doctest.testmod()


# 或者使用内置的Python函数sum()和内置的Python函数range()
def sum_to_n(n: int):
    return sum(range(1, n+1))


if __name__ == "__main__":
    import doctest
    doctest.testmod()


# 或者使用数学公式，n*(n+1)/2
def sum_to_n(n: int):
    return n * (n+1) // 2


if __name__ == "__main__":
    import doctest
    doctest.testmod()


# 或者使用for循环
def sum_to_n(n: int):
    s = 0
    for i in range(1, n+1):
        s += i
    return s


if __name__ == "__main__":
    import doctest
    doctest.testmod()


# 或者使用while循环
def sum_to_n(n: int):
    s = 0
    i = 1
    while i <= n:
        s += i
        i += 1
    return s


if __name__ == "__main__":
    import doctest
    doctest.testmod()


# 或者使用列表推导式
def sum_to_n(n: int):
    return sum([i for i in range(1, n+1)])


if __name__ == "__main__":
    import doctest
    doctest.testmod()


# 或者使用递归
def sum_to_n(n: int):
    if n == 1:
        return 1
    else:
        return n + sum_to_n(n-1)


if __name__ == "__main__":
    import doctest
    doctest.testmod()

