def last_Digit_Factorial(n):
    if n == 0:
        return 1
    fact = 1
    for i in range(1, n+1):
        fact *= i
        while fact % 10 == 0:
            fact /= 10
        fact %= 10
    return int(fact % 10)

print(last_Digit_Factorial(4))

#Test Cases
assert last_Digit_Factorial(4) == 4
assert last_Digit_Factorial(5) == 0
assert last_Digit_Factorial(6) == 4
assert last_Digit_Factorial(7) == 2
assert last_Digit_Factorial(8) == 4
assert last_Digit_Factorial(9) == 8
assert last_Digit_Factorial(10) == 4
assert last_Digit_Factorial(11) == 4
assert last_Digit_Factorial(12) == 8
assert last_Digit_Factorial(13) == 0
assert last_Digit_Factorial(14) == 4
assert last_Digit_Factorial(15) == 8
assert last_Digit_Factorial(16) == 4
assert last_Digit_Factorial(17) == 4
assert last_Digit_Factorial(18) == 4
assert last_Digit_Factorial(19) == 8
assert last_Digit_Factorial(20) == 4
assert last_Digit_Factorial(21) == 2
assert last_Digit_Factorial(22) == 4
assert last_Digit_Factorial(23) == 6
assert last_Digit_Factorial(24) == 4
assert last_Digit_Factorial(25) == 0
assert last_Digit_Factorial(26) == 4
assert last_Digit_Factorial(27) == 2
assert last_Digit_Factorial(28) == 4
assert last_Digit_Factorial(29) == 6
assert last_Digit_Factorial(30) == 4
assert last_Digit_Factorial(