You can use the `match` method to split the number into an array of digits, then use `filter` to count the number of even and odd digits respectively. Here is the solution:

```javascript
const evenOddCount = (num) => {
  const digits = Math.abs(num).toString().match(/\d/g);
  const evenDigits = digits.filter(digit => digit % 2 === 0);
  const oddDigits = digits.filter(digit => digit % 2 !== 0);
  return [evenDigits.length, oddDigits.length];
}
```

This solution first converts the number to a string with the `toString` method, then uses the `match` method with a regular expression to split the string into an array of digits. The `/\d/g` regular expression matches any digit character.

Then, the solution uses the `filter` method to count the number of even and odd digits. The `filter` method takes a function as an argument, which is called for each digit in the array. The function returns `true` if the digit is even or odd, and `false` otherwise.

Finally, the solution returns an array with the counts of even and odd digits.

Note that the `Math.abs` method is used to convert the number to a positive number before converting it to a string, so that negative numbers are handled correctly.