You can solve this problem by using the `reduce` method to keep track of the largest and smallest integers. Here's the solution:

```javascript
const largestSmallestIntegers = (lst) => {
  return lst.reduce((acc, val) => {
    if (val < 0) {
      if (acc[0] === null || val > acc[0]) {
        acc[0] = val;
      }
    } else if (val > 0) {
      if (acc[1] === null || val < acc[1]) {
        acc[1] = val;
      }
    }
    return acc;
  }, [null, null]);
};
```

The `reduce` method iterates over the list and updates the `acc` array with the largest and smallest integers. The initial value of `acc` is `[null, null]`, which represents that there are no negative or positive integers found so far.

The `reduce` function checks if the current value (`val`) is negative or positive. If it's negative, it updates the first element of `acc` if it's `null` or if the current value is larger than the current largest negative integer. If it's positive, it updates the second element of `acc` if it's `null` or if the current value is smaller than the current smallest positive integer.

Finally, the function returns the `acc` array, which contains the largest negative integer (if any) and the smallest positive integer (if any).