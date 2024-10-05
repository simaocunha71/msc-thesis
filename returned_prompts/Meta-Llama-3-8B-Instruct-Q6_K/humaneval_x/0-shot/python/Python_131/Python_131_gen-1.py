    def digits(n):
        product = 1
        for digit in str(n):
            if int(digit) % 2 != 0:
                product *= int(digit)
        return product if product != 1 else 0
    # test the function
    print(digits(1))  # 1
    print(digits(4))   # 0
    print(digits(235)) # 15
    print(digits(12345)) # 15
    print(digits(11111)) # 1
    print(digits(22222)) # 0
    print(digits(10001)) # 1
    print(digits(111111)) # 1
    print(digits(222222)) # 0
    print(digits(123456)) # 3
    print(digits(234567)) # 15
    print(digits(1234567)) # 15
    print(digits(12345678)) # 15
    print(digits(123456789)) # 45
    print(digits(1234567890)) # 0
    print(digits(111111111)) # 1
    print(digits(222222222)) # 0
    print(digits(333333333)) # 3
    print(digits(1111111111)) # 1
    print(digits(2222222222)) # 0
    print(digits(3333333333)) # 3
    print(digits(11111111111)) # 1
    print(digits(22222222222)) # 0
    print(digits(33333333333)) # 3
    print(digits(111111111111)) # 1
    print(digits(222222222222)) # 0
    print(digits(333333333333)) # 3
    print(digits(1111111111111)) # 1
    print(digits(2222222222222)) # 0
    print(digits(3333333333333)) # 3
    print(digits(11111111111111)) # 1
    print(digits(22222222222222)) # 0
    print(digits(33333333333333)) # 3
    print(digits(111111111111111)) # 1
    print(digits(222222222222222)) # 0
    print(digits(333333333333333)) # 3
    print(digits(111111111111