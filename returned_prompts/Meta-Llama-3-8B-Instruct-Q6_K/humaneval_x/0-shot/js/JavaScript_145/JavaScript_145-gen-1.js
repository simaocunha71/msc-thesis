```
const orderByPoints = (nums) => {
  return nums.sort((a, b) => {
    const sumA = a.toString().split('').reduce((acc, curr) => acc + parseInt(curr), 0);
    const sumB = b.toString().split('').reduce((acc, curr) => acc + parseInt(curr), 0);
    if (sumA === sumB) {
      return nums.indexOf(a) - nums.indexOf(b);
    } else {
      return sumA - sumB;
    }
  });
};
```
This function sorts the given list of integers in ascending order according to the sum of their digits. If there are several items with similar sum of their digits, it orders them based on their index in the original list.

Here is how it works:

1. It loops through each number in the list.
2. For each number, it calculates the sum of its digits by converting the number to a string, splitting it into individual digits, and then summing up the digits.
3. It sorts the list based on the sum of the digits.
4. If there are several items with similar sum of their digits, it compares their original indices in the list and orders them based on those indices.

For example, if you call `orderByPoints([1, 11, -1, -11, -12])`, the function will return `[-1, -11, 1, -12, 11]`. If you call `orderByPoints([])`, the function will return an empty list.