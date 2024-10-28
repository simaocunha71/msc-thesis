To solve this problem, you can follow these steps:

1. Convert the decimal number N to a binary number. In JavaScript, you can use the `toString(2)` method to convert a number to a binary string. For example, `1000.toString(2)` will return `"1100000"`.

2. Iterate over each digit in the binary string and add up the decimal values of the digits. You can use the `map()` method to convert each binary digit to its decimal value and then use the `reduce()` method to sum up all the values. For example, `[1, 1, 0, 0, 0, 0, 0, 0].map(digit => parseInt(digit)).