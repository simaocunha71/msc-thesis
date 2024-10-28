You can create a helper function `getSumOfDigits` to calculate the sum of digits for each number. Then, use the `sort` method on the input array and compare the sum of digits of each number to sort them in ascending order.

Here is the complete solution:

```javascript
const orderByPoints = (nums) => {
  const getSumOfDigits = (num) => {
    return Math.abs(num).toString().split('').reduce((acc, digit) => acc + +digit, 0);
  }
  return nums.sort((a, b) => {
    const sumA = getSumOfDigits(a);
    const sumB = getSumOfDigits(b);
    if (sumA === sumB) {
      return nums.indexOf(a) - nums.indexOf(b);
    }
    return sumA - sumB;
  });
}
```

In this solution, `getSumOfDigits` is a helper function that calculates the sum of digits for a given number. The `sort` method is used on the input array `nums` to sort the numbers based on the sum of their digits. If the sum of digits for two numbers is the same, the index of the first occurrence of these numbers in the original array is used for comparison.