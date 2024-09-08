    The problem can be divided into two parts: 
    1. Convert the integer into binary.
    2. Calculate the sum of the binary digits.
    The binary conversion is done using a while loop, where the remainder of the integer divided by 2 is used to construct the binary string. The integer is then divided by 2 for the next iteration.
    The sum of the binary digits is calculated by iterating over the binary string and adding each digit to a running total.
    The function `solve` returns a string representation of the sum.
    In the main function, the user is prompted to enter a number, and the `solve` function is called with this number. The result is then printed to the console.
}

