I used the following conditions to check the type of input:
1. If both inputs are numbers, return the larger number.
2. If both inputs are strings, use parseFloat() to convert them to numbers and then compare. Replace the comma with nothing to remove it.
3. If one input is a number and the other is a string, convert the string to a number using parseFloat() and then compare.
4. If one input is a string and the other is a number, convert the string to a number using parseFloat() and then compare.
5. If the inputs are of different types, return null.