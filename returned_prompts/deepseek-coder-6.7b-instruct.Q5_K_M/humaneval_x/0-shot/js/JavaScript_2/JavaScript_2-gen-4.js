  return number - Math.floor(number);
}

console.log(truncateNumber(3.5)); // 0.5

In the code, we subtract the floor of the number from the original number. The floor function in JavaScript returns the largest integer less than or equal to a given number. Since the floor function returns the largest integer that is less than or equal to the number, subtracting it from the number will give us the decimal part of the number.

In the test case, we call the function with the argument 3.5. The function returns 3.5 - 3 = 0.5, so 0.5 is printed to the console.

This solution assumes that the input number is a positive floating point number. If the input number is not a positive floating point number, the behavior of the function is undefined.

Note:
It's a very basic solution and can be improved by checking the input and handling edge cases properly.
*/

const truncateNumber = (number) => {
  if (number < 0) {
    throw new Error('Input must be a positive floating point number');
  }

  if (!Number.isFinite(number)) {
    throw new Error('Input must be a finite number');
  }

  return number - Math.floor(number);
}

console.log(truncateNumber(3.5)); // 0.5
console.log(truncateNumber(-3.5)); // throws an error
console.log(truncateNumber(Infinity)); // throws an error
```

This solution first checks if the input number is negative or infinite, and throws an error if it is. It then returns the decimal part of the number as before. This ensures that the function behaves as expected for all valid inputs.

Note that this solution does not handle the case where the input is a non-numeric value. If you need to handle such cases, you would need to add additional error checking code.

Also, this solution does not handle the case where the input is a floating point number that is very close to but not exactly equal to an integer. For example, if the input is 3.0, the function will return 0.0 instead of 3.0 - 3 = 0.0. If you need to