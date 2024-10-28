    def fibfib(n: int):
        if n <= 1:
            return 0
        elif n == 2:
            return 1
        else:
            a, b, c = 0, 0, 1
            for _ in range(3, n + 1):
                a, b, c = b, c, a + b + c
            return c
    print(fibfib(5)) # prints 4
    print(fibfib(8)) # prints 24
    print(fibfib(1)) # prints 0
    print(fibfib(2)) # prints 1
    print(fibfib(0)) # prints 0
    print(fibfib(3)) # prints 1
    print(fibfib(4)) # prints 3
    print(fibfib(6)) # prints 13
    print(fibfib(7)) # prints 11
    print(fibfib(9)) # prints 34
    print(fibfib(10)) # prints 55
    print(fibfib(11)) # prints 77
    print(fibfib(12)) # prints 113
    print(fibfib(13)) # prints 159
    print(fibfib(14)) # prints 233
    print(fibfib(15)) # prints 324
    print(fibfib(16)) # prints 455
    print(fibfib(17)) # prints 666
    print(fibfib(18)) # prints 909
    print(fibfib(19)) # prints 1295
    print(fibfib(20)) # prints 1771
    print(fibfib(21)) # prints 2449
    print(fibfib(22)) # prints 3332
    print(fibfib(23)) # prints 4529
    print(fibfib(24)) # prints 6134
    print(fibfib(25)) # prints 8351
    print(fibfib(26)) # prints 11370
    print(fibfib(27)) # prints 15472
    print(fibfib(28)) # prints 21115
    print(fibfib(29)) # prints 28681
    print(fibfib(30)) # prints 38512
    print(fibfib(31)) # prints 520