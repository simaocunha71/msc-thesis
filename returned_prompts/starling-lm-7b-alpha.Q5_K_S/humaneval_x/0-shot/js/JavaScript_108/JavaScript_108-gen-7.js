Here's a function `countNums` that takes an array of integers and returns the number of elements with a sum of digits greater than 0.

The function uses a helper function `sumOfDigits` to calculate the sum of digits of a number. This function takes a number `n` as input and converts it to a string. Then, it iterates over the string from right to left, converting each character to a number and adding it to the sum. Finally, it returns the sum.

The `countNums` function initializes a variable `count` to keep track of the number of elements with a sum of digits greater than 0. It then uses the `forEach` method to iterate over each element in the input array. For each element, it calls the `sumOfDigits` function to calculate the sum of its digits. If the sum is greater than 0, it increments the `count` variable. After iterating over all the elements, the function returns the final value of `count`.

To test the function, you can use the provided test cases. For example, `countNums([])` should return 0, `countNums([-1, 11, -11])` should return 1, and `countNums([1, 1, 2])` should return 3.

Overall, this function correctly counts the number of elements in an array of integers that have a sum of digits greater than 0.

*/

