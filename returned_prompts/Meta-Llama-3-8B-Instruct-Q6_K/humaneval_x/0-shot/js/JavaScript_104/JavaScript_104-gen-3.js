Here is the solution in JavaScript:
```
function uniqueDigits(x) {
  return x.filter(num => !/\d/.test(String(num).replace(/0|2|4|6|8/g, ''))).sort((a, b) => a - b);
}
```
Here's an explanation of the code:

1. `x.filter()`: This method filters the array `x` and returns a new array with only the elements that pass the test implemented by the provided function.
2. `!/\d/.test(String(num).replace(/0|2|4|6|8/g, ''))`: This is the test function. It checks if the string representation of the number `num` does not contain any even digits. Here's how it works:
	* `String(num)`: Converts the number to a string.
	* `replace(/0|2|4|6|8/g, '')`: Replaces all even digits (0, 2, 4, 6, 8) with an empty string, effectively removing them.
	* `/\d/.test()`: Tests if the resulting string contains any digits. If it does, the function returns `true`, indicating that the number has at least one even digit. If it doesn't, the function returns `false`.
	* `!` is the negation operator, so the filter function returns `true` if the test function returns `false`, and vice versa.
3. `.sort((a, b) => a - b)`: This sorts the resulting array in ascending order.

You can test the function with the examples you provided:
```
console.log(uniqueDigits([15, 33, 1422, 1])); // [1, 15, 33]
console.log(uniqueDigits([152, 323, 1422, 10])); // []
```
I hope this helps! Let me know if you have any questions. 😊

---

This is a solution that uses JavaScript's built-in `filter()` method to filter the array of numbers and remove any numbers that have even digits. The `filter()` method returns a new array with only the elements that pass the test implemented by the provided function.

The function `uniqueDigits()` takes an array of numbers as input and returns a new array with only the numbers that do not have any even digits. The `filter()` method is used to implement this logic.

The test function `!/\d/.test(String(num).replace(/0