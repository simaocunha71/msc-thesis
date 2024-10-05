Here is the JavaScript function that meets the requirements:

```javascript
const largestSmallestIntegers = (lst) => {
  let maxNegative = null;
  let minPositive = null;

  for (let i = 0; i < lst.length; i++) {
    if (lst[i] < 0 && (maxNegative === null || lst[i] > maxNegative)) {
      maxNegative = lst[i];
    } else if (lst[i] > 0 && (minPositive === null || lst[i] < minPositive)) {
      minPositive = lst[i];
    }
  }

  if (maxNegative !== null && minPositive !== null) {
    return [maxNegative, minPositive];
  } else {
    return [null, null];
  }
};
```

Here's a breakdown of how this function works:

1. Initialize two variables `maxNegative` and `minPositive` to null. These will store the largest negative integer and the smallest positive integer found in the list, respectively.
2. Iterate through the list using a for loop.
3. For each element in the list, check if it's a negative integer and if it's larger than the current `maxNegative`. If it is, update `maxNegative`.
4. For each element in the list, check if it's a positive integer and if it's smaller than the current `minPositive`. If it is, update `minPositive`.
5. After iterating through the list, check if both `maxNegative` and `minPositive` are not null. If they are, return a list containing `maxNegative` and `minPositive`. Otherwise, return a list containing two null values.

This function should work correctly for the examples provided in the problem statement. Let me know if you have any questions or need further clarification!