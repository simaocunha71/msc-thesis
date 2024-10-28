```
const multiply = (a, b) => {
  return (a % 10) * (b % 10);
};
```


This function takes two integers `a` and `b` as input, and returns the product of their unit digits. It does this by using the modulus operator `%` to extract the last digit of each number (i.e., the unit digit), and then multiplying these two digits together. 

For example, if `a` is 148 and `b` is 412, the function will return `(8 * 2) = 16`. If `a` is 19 and `b` is 28, the function will return `(9 * 8) = 72`. If `a` is 2020 and `b` is 1851, the function will return `(0 * 1) = 0`. If `a` is 14 and `b` is -15, the function will return `(4 * (-5)) = 20`. 

This function assumes that the input is always valid, meaning that it does not check for invalid input such as non-integer values or very large integers that may exceed the maximum value that can be represented by the modulus operator. 

Note that this function does not handle the case where the input is negative. If the input can be negative, the function should be modified to handle this case. For example, the function could add a check at the beginning to see if either `a` or `b` is negative, and if so, return the product of the absolute values of the two numbers. 