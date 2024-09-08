def last_Digit_Factorial(n):
    factorial = 1
    for i in range(1, n+1):
        factorial *= i
        while factorial % 10 == 0:
            factorial /= 10
        factorial = int(factorial % 100000)
    return factorial % 10 if factorial else 0

print(last_Digit_Factorial(4))

#Note: The program uses a while loop to remove trailing zeros from the factorial. The factorial of a number is often very large, so we only keep the last five digits of the factorial by taking the modulus 100000. If the factorial is 0, the function returns 0.

#The time complexity of this function is O(n), and the space complexity is O(1).

#The function works by iterating from 1 to n (inclusive), multiplying the current factorial by the current number, and then reducing the factorial to its last five digits. The last digit of the factorial is then returned. If the factorial is 0, the function returns 0.

#The function uses a while loop to remove trailing zeros from the factorial. The factorial of a number is often very large, so we only keep the last five digits of the factorial by taking the modulus 100000. If the factorial is 0, the function returns 0.

#The time complexity of this function is O(n), and the space complexity is O(1).

#The function works by iterating from 1 to n (inclusive), multiplying the current factorial by the current number, and then reducing the factorial to its last five digits. The last digit of the factorial is then returned. If the factorial is 0, the function returns 0.

#The function uses a while loop to remove trailing zeros from the factorial. The factorial of a number is often very large, so we only keep the last five digits of the factorial by taking the modulus 100000. If the factorial is 0, the function returns 0.

#The time complexity of this function is O(n