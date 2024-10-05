Here is a JavaScript solution for the problem:

```javascript
const largestSmallestIntegers = (lst) => {
  let maxNegative = null;
  let minPositive = null;

  lst.forEach((num) => {
    if (num < 0 && (maxNegative === null || num > maxNegative)) {
      maxNegative = num;
    } else if (num > 0 && (minPositive === null || num < minPositive)) {
      minPositive = num;
    }
  });

  if (maxNegative === null && minPositive === null) {
    return [null, null];
  } else if (maxNegative === null) {
    return [null, minPositive];
  } else if (minPositive === null) {
    return [maxNegative, null];
  } else {
    return [maxNegative, minPositive];
  }
};
```

This function iterates through the input list, keeping track of the largest negative integer and the smallest positive integer it finds. If it finds no negative integers, it sets `maxNegative` to `null`. If it finds no positive integers, it sets `minPositive` to `null`. Finally, it returns a list containing `maxNegative` and `minPositive`, or `null` if either of them is `null`. If both are `null`, it returns `[null, null]`.