def last_Digit_Factorial(num):
    if(num == 0):
        return 1
    else:
        last_Digit_Factorial = 1
        for i in range(1, num + 1):
            last_Digit_Factorial = (last_Digit_Factorial * i) % 10
        return last_Digit_Factorial

# Driver program
print(last_Digit_Factorial(4))




"""
Time complexity: O(N)
Space complexity: O(1)
"""






"""
The time complexity of the above program is O(n) because the program uses a for loop that runs n times, where n is the input number. The space complexity is O(1) because the program uses a constant amount of additional space to store the result.

The time complexity of O(n) means that the program's running time increases linearly with the input size. As the input number increases, the program takes more time to run. The space complexity of O(1) means that the program's memory usage remains constant regardless of the input size.

In this program, the last_Digit_Factorial function is used to calculate the last digit of the factorial of a given number. The function uses a for loop to iterate through the numbers from 1 to the input number. For each iteration, the function multiplies the current number with the result stored in the last_Digit_Factorial variable, and then takes the modulus 10 to get the last digit of the product. The result is stored in the last_Digit_Factorial variable. Finally, the function returns the last_Digit_Factorial value, which is the last digit of the factorial of the input number.

The driver program then calls the last_Digit_Factorial function with the input number 4 and prints the result. In this case, the result is 4, which is the last digit of the factorial of 4.
"""





























































