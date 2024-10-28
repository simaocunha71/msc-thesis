
    def even_odd_count(num):
        num = str(abs(num))
        even = sum(1 for digit in num if int(digit) % 2 == 0)
        odd = sum(1 for digit in num if int(digit) % 2 != 0)
        return (even, odd)

    print(even_odd_count(-12))  # ==> (1, 1)
    print(even_odd_count(123))  # ==> (1, 2)

    # alternative solution
    def even_odd_count(num):
        num = str(abs(num))
        return (sum(1 for digit in num if int(digit) % 2 == 0), sum(1 for digit in num if int(digit) % 2 != 0))

    print(even_odd_count(-12))  # ==> (1, 1)
    print(even_odd_count(123))  # ==> (1, 2)

    # alternative solution
    def even_odd_count(num):
        num = str(abs(num))
        return (sum(digit in '02468' for digit in num), sum(digit in '13579' for digit in num))

    print(even_odd_count(-12))  # ==> (1, 1)
    print(even_odd_count(123))  # ==> (1, 2)

    # alternative solution
    def even_odd_count(num):
        num = str(abs(num))
        even = len([digit for digit in num if int(digit) % 2 == 0])
        odd = len([digit for digit in num if int(digit) % 2 != 0])
        return (even, odd)

    print(even_odd_count(-12))  # ==> (1, 1)
    print(even_odd_count(123))  # ==> (1, 2)

    # alternative solution
    def even_odd_count(num):
        num = str(abs(