```javascript
const uniqueDigits = (x) => {
    return x
      .filter(num => !num.toString().includes('2') && !num.toString().includes('4') && !num.toString().includes('6') && !num.toString().includes('8') && !num.toString().includes('0'))
      .sort((a, b) => a - b);
};
```
Explanation:
We use the `filter()` method to create a new array with only the numbers that do not have any even digits (i.e., 2, 4, 6, 8, or 0). We do this by checking if the string representation of each number includes any of these digits using the `includes()` method. If a number passes this filter, it is added to the new array.

After filtering, we use the `sort()` method to sort the array in ascending order. We compare each pair of numbers using the `-` operator, which returns the difference between the two numbers. The array is sorted based on these differences.

The final result is a sorted array of numbers that do not have any even digits. If no such numbers exist, the array will be empty. For example, given the input `[152, 323, 1422, 10]`, the output would be an empty array `[]`. If the input is `[15, 33, 1422, 1]`, the output would be `[1, 15, 33]`.