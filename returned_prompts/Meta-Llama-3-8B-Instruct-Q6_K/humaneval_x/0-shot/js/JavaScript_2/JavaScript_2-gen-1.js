Here is the solution in JavaScript:
```
const truncateNumber = (number) => {
  return number - Math.floor(number);
}
```
Here's an explanation of the code:

* We use the `Math.floor()` function to get the largest integer smaller than the given number.
* We subtract this integer from the original number to get the decimal part.
* The result is the decimal part of the number.

You can test this function with the example you provided:
```
console.log(truncateNumber(3.5)); // Output: 0.5
```
This function works for any positive floating point number. If you want to handle negative numbers as well, you can add a simple check:
```
const truncateNumber = (number) => {
  if (number < 0) {
    return -(-number - Math.floor(-number));
  } else {
    return number - Math.floor(number);
  }
}
```
This code checks if the number is negative, and if so, it uses the same logic as before but with the absolute value of the number. If the number is positive, it simply subtracts the integer part from the original number.