  let evenCount = 0, oddCount = 0;
  let numArr = Math.abs(num).toString().split('');
  numArr.forEach(digit => digit % 2 === 0 ? evenCount++ : oddCount++);
  return [evenCount, oddCount];
};

console.log(evenOddCount(-12)); // ==> [1, 1]
console.log(evenOddCount(123)); // ==> [1, 2]

```

## Code Explanation:

This solution works by first converting the input number to a string and splitting it into an array of individual digits. Then it counts the number of even and odd digits and returns these counts as an array.

It uses the `Math.abs()` function to ensure that the input number is positive, as negative numbers can also have even and odd digits.

The `forEach()` function is used to iterate over each digit in the array. The `%` operator is used to check if the digit is even (i.e., if it is divisible by 2). If it is, the `evenCount` is incremented by 1; otherwise, the `oddCount` is incremented by 1.

Finally, the counts of even and odd digits are returned as an array.

## Complexity Analysis:

The time complexity of this solution is O(n), where n is the number of digits in the input number. This is because we are traversing the array of digits once.

The space complexity is also O(n), because in the worst case, we are storing the digits of the input number in an array.

## References:

- [Array.prototype.split()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/split)
- [Array.prototype.forEach()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/forEach)
- [Arithmetic operators in JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Arithmetic_Operators)
- [Comparison