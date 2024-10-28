Here is a simple JavaScript function that solves the problem:

```javascript
const uniqueDigits = (x) => {
  return x.filter(num => !/[2,4,6,8]/.test(String(num))).sort((a, b) => a - b);
};
```

This function works by first filtering the input array to only include numbers that don't have any even digits. It does this by using a regular expression to check if any of the digits in the number are 2, 4, 6, or 8. The `String(num)` is used to convert the number to a string so that the regular expression can be used to check each digit.

The filtered array is then sorted in ascending order using the `sort()` function with a compare function that subtracts the two numbers and returns the result.

Here's an example of how you could use this function:

```javascript
console.log(uniqueDigits([15, 33, 1422, 1])); // [1, 15, 33]
console.log(uniqueDigits([152, 323, 1422, 10])); // []
```


This function assumes that the input array only contains positive integers. If the input array can contain non-positive integers or non-integer values, you may need to add additional error checking code.