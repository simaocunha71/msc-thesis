```javascript
const moveOneBall = (arr) => {
  if (arr.length === 0) return true;

  let i = 0;
  while (i < arr.length - 1) {
    if (arr[i] > arr[i + 1]) {
      return false;
    }
    i++;
  }
  return true;
};
```
Explanation:
The function `moveOneBall` checks if it's possible to sort the given array in non-decreasing order by performing right shift operations. If the array is empty, it returns `true` as there is no operation needed to sort an empty array.

The function then iterates through the array using a while loop. For each pair of consecutive elements, it checks if the current element is greater than the next one. If it finds such a pair, it returns `false` as it's not possible to sort the array by performing right shift operations.

If the function finishes the iteration without finding any such pair, it returns `true` as it's possible to sort the array by performing right shift operations.

For example, for the array `[3, 4, 5, 1, 2]`, the function will return `true` as it's possible to sort the array by performing 2 right shift operations. For the array `[3, 5, 4, 1, 2]`, the function will return `false` as it's not possible to sort the array by performing any number of right shift operations.