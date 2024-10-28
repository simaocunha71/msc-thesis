The function can be implemented by using the modulo operator to get the unit digits of both numbers and then multiplying them together. Here is the implementation in JavaScript:
```
const multiply = (a, b) => {
  return ((a % 10) * (b % 10));
}
```
This function works by using the modulo operator (`%`) to get the remainder of the division of `a` and `b` by 10, which gives the unit digits of `a` and `b` respectively. Then it multiplies these two unit digits together and returns the result. 

For example, if `a` is 148 and `b` is 412, the function will return `((148 % 10) * (412 % 10)) = (8 * 2) = 16`. Similarly, if `a` is 19 and `b` is 28, the function will return `((19 % 10) * (28 % 10)) = (9 * 8) = 72`. If `a` is 2020 and `b` is 1851, the function will return `((2020 % 10) * (1851 % 10)) = (0 * 1) = 0`. If `a` is 14 and `b` is -15, the function will return `((14 % 10) * (-15 % 10)) = (4 * (-5)) = 20`. 

This function assumes that the input is always valid, i.e., it always expects two integers as input. It does not check if the input is valid or not. If you want to add error handling to the function, you can do so by checking if the input is a number and if it is within a certain range. For example:
```
const multiply = (a, b) => {
  if (typeof a !== 'number' || typeof b !== 'number') {
    throw new Error('Input must be a number');
  }
  if (a < 0 || b < 0) {
    throw new Error('Input must be a non-negative number');
  }
  return ((a % 10) * (b % 10));
}
```
This version of the function will throw an error if the input is not a number or if it is a negative number. You can modify the error handling to suit your needs. 