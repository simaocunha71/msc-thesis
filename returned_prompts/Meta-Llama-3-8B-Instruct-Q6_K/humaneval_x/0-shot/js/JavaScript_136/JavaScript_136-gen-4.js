Here is the JavaScript solution for the problem:

```javascript
const largestSmallestIntegers = (lst) => {
  if (!lst.length) return [null, null]; // If the list is empty, return [null, null]
  
  let maxNegative = null;
  let minPositive = null;

  for (let i = 0; i < lst.length; i++) {
    if (lst[i] < 0) {
      if (maxNegative === null || lst[i] > maxNegative) {
        maxNegative = lst[i]; // Update maxNegative if it's a larger negative number
      }
    } else if (lst[i] > 0) {
      if (minPositive === null || lst[i] < minPositive) {
        minPositive = lst[i]; // Update minPositive if it's a smaller positive number
      }
    }
  }

  return [maxNegative !== null ? maxNegative : null, minPositive !== null ? minPositive : null];
};
```

This function iterates over the input list. If it finds a negative number, it checks if it's larger than the current maxNegative. If it is, it updates maxNegative. Similarly, if it finds a positive number, it checks if it's smaller than the current minPositive. If it is, it updates minPositive. Finally, it returns an array with the largest negative number (or null if no negative numbers were found) and the smallest positive number (or null if no positive numbers were found). If the list is empty, it returns [null, null]. If the list contains only zeros, it also returns [null, null].