To obtain the signed digits of a number, the function uses the `strconv.Itoa()` function which converts an integer to its string representation. The `abs()` function is then used to get the absolute value of the number. This is done by taking the difference between the original number and the negative of the original number. 

To obtain the length of a string, the `len()` function is used. In this case, it is used on the string representation of the absolute value of the number. The `-1` is subtracted from the length of the string to account for the sign digit of the number.

The `abs()` function works by returning the non-negative value of an integer. In other words, it converts a negative number to a positive number.

Here's a breakdown of the steps in the `CountNums` function:

1. Initialize a variable `res` to 0. This variable will store the count of numbers with a sum of digits greater than 0.

2. Use a `for` loop to iterate over each element in the `arr` slice.

3. Inside the loop, convert the absolute value of the current element to a string using `strconv.Itoa(abs(e))`. The `abs()` function is used to get the absolute value of the element, and `strconv.Itoa()` is used to convert this value to a string.

4. Calculate the length of the string representation of the absolute value using `len(strconv.Itoa(abs(e)))`. This gives the total number of digits in the absolute value of the current element.

5. Subtract 1 from the length of the string to account for the sign digit of the number.