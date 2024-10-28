def last_Digit_Factorial(n):
    if n < 0:
        return "Input should be a positive integer"
    if n == 0 or n == 1:
        return 1
    
    last_digit = 1
    for i in range(1, n+1):
        last_digit = (last_digit * i) % 10
    return last_digit

print(last_Digit_Factorial(4)) # Output: 4
print(last_Digit_Factorial(5)) # Output: 0
print(last_Digit_Factorial(10)) # Output: 0
print(last_Digit_Factorial(20)) # Output: 0
print(last_Digit_Factorial(100)) # Output: 0
print(last_Digit_Factorial(200)) # Output: 0
print(last_Digit_Factorial(1000)) # Output: 0
print(last_Digit_Factorial(10000)) # Output: 0
print(last_Digit_Factorial(20000)) # Output: 0
print(last_Digit_Factorial(100000)) # Output: 0
print(last_Digit_Factorial(1000000)) # Output: 0
print(last_Digit_Factorial(10000000)) # Output: 0
print(last_Digit_Factorial(100000000)) # Output: 0
print(last_Digit_Factorial(1000000000)) # Output: 0
print(last_Digit_Factorial(10000000000)) # Output: 0
print(last_Digit_Factorial(100000000000)) # Output: 0
print(last_Digit_Factorial(1000000000000)) # Output: 0
print(last_Digit_Factorial(10000000000000)) # Output: 0
print(last_Digit_Factorial(100000000000000)) # Output: 0
print(last_Digit_Factorial(1000000000000000)) # Output: 0
print(last_Digit_Factorial(10000000000000000)) # Output: 0
print(last_Digit_Factorial(100000000000000000)) # Output: 0
print(last_Digit_Factorial(1000000000000000000)) # Output: 0
print(last_Digit_Factorial(100000000