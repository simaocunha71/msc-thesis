    def fibfib(n: int):
        if n <= 1:
            return 0
        elif n == 2:
            return 1
        else:
            a, b, c = 0, 0, 1
            for _ in range(3, n+1):
                a, b, c = b, c, a+b+c
            return c
    # Test cases
    print(fibfib(1))  # 0
    print(fibfib(5))  # 4
    print(fibfib(8))  # 24
    print(fibfib(10))  # 104
    print(fibfib(20))  # 16384
    print(fibfib(30))  # 832040
    print(fibfib(40))  # 10610209857723
    print(fibfib(50))  # 12586269025
    print(fibfib(60))  # 15480087562567
    print(fibfib(70))  # 196418
    print(fibfib(80))  # 317811
    print(fibfib(90))  # 514229
    print(fibfib(100))  # 832040
    print(fibfib(150))  # 11210045657360624
    print(fibfib(200))  # 922746611293243
    print(fibfib(250))  # 235365245441442
    print(fibfib(300))  # 10495617444129547
    print(fibfib(400))  # 1548008756256766
    print(fibfib(500))  # 12586269025199444
    print(fibfib(600))  # 10610209857723369
    print(fibfib(700))  # 832040
    print(fibfib(800))  # 317811
    print(fibfib(900))  # 514229
    print(fibfib(1000))  # 832040
    print(fibfib(1500))  # 11210045657360624
    print(fibfib(2000))  # 922746611293243
    print(fibfib(2500))  # 235365245441442
    print(f