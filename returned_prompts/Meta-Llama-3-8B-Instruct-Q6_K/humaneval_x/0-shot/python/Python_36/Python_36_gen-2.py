def fizz_buzz(n: int):
    count = 0
    for i in range(1, n):
        if i % 11 == 0 or i % 13 == 0:
            str_i = str(i)
            count += str_i.count('7')
    return count
# Test cases
print(fizz_buzz(50))  # Expected output: 0
print(fizz_buzz(78))  # Expected output: 2
print(fizz_buzz(79))  # Expected output: 3
# Explanation: The function takes an integer n as input and returns the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13. It does this by iterating over all integers less than n, checking if each integer is divisible by 11 or 13, and if so, converting it to a string to count the number of occurrences of the digit 7. The function returns the total count. The test cases demonstrate the function's correctness.