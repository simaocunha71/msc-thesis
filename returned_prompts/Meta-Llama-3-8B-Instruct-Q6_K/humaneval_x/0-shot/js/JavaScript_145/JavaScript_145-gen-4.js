Here is a solution for the problem:
```
const orderByPoints = (nums) => {
  return nums.sort((a, b) => {
    const sumA = a.toString().split('').reduce((acc, curr) => acc + parseInt(curr), 0);
    const sumB = b.toString().split('').reduce((acc, curr) => acc + parseInt(curr), 0);
    if (sumA === sumB) {
      return nums.indexOf(a) - nums.indexOf(b);
    }
    return sumA - sumB;
  });
};
```
This function uses the built-in `sort()` method of JavaScript arrays, and provides a compare function as an argument. This compare function calculates the sum of the digits of each number, and if the sums are equal, it compares the original indices of the numbers in the list. The `indexOf()` method is used to get the index of each number in the original list. The `reduce()` method is used to calculate the sum of the digits of each number. The `toString()` method is used to convert each number to a string, and the `split('')` method is used to split each string into an array of digits. The `parseInt()` method is used to convert each digit back to an integer. The `acc + parseInt(curr)` expression is used to accumulate the sum of the digits. The `if (sumA === sumB)` statement checks if the sums of the digits are equal, and if they are, it returns the difference between the original indices of the numbers. If the sums are not equal, it returns the difference between the sums. The `sort()` method returns a new array with the elements in the sorted order.