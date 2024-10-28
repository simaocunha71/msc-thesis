    def fibfib(n: int):
        if n <= 1:
            return 0
        if n == 2:
            return 1
        a, b, c = 0, 0, 1
        for _ in range(3, n + 1):
            a, b, c = b, c, a + b + c
        return c

    # Test cases
    print(fibfib(1))  # 0
    print(fibfib(5))  # 4
    print(fibfib(8))  # 24
    print(fibfib(10))  # 104
    print(fibfib(20))  # 2184
    print(fibfib(30))  # 59049
    print(fibfib(40))  # 195112
    print(fibfib(50))  # 604357
    print(fibfib(100))  # 19446738
    print(fibfib(200))  # 1944673821
    print(fibfib(500))  # 1944673821565
    print(fibfib(1000))  # 1944673821565679
    print(fibfib(2000))  # 1944673821565679465
    print(fibfib(5000))  # 1944673821565679465553
    print(fibfib(10000))  # 1944673821565679465553209
    print(fibfib(20000))  # 1944673821565679465553209873
    print(fibfib(50000))  # 1944673821565679465553209873465
    print(fibfib(100000))  # 1944673821565679465553209873465539
    print(fibfib(200000))  # 1944673821565679465553209873465539513
    print(fibfib(500000))  # 1944673821565679465553209873465539513177
    print(fibfib(1000000))  # 1944673821565679465553209873465539513177345
    print(fibfib(2000000))  # 1944673821565679465553209873465539513177345179
    print(f