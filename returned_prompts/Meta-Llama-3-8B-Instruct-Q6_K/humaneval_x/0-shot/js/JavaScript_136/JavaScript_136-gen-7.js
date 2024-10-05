Here is a JavaScript solution for the problem:

```javascript
const largestSmallestIntegers = (lst) => {
  if (lst.length === 0) {
    return [null, null];
  }

  const negatives = lst.filter(num => num < 0);
  const positives = lst.filter(num => num > 0);

  if (negatives.length === 0) {
    return [null, Math.min(...positives)];
  } else if (positives.length === 0) {
    return [Math.max(...negatives), null];
  } else {
    return [Math.max(...negatives), Math.min(...positives)];
  }
};
```

The function `largestSmallestIntegers` takes an array of integers as an argument. It first checks if the array is empty. If it is, the function returns an array with two `null` values.

Then, it filters the array to get the negative and positive integers. If there are no negative integers, it returns an array with the smallest positive integer and `null`. If there are no positive integers, it returns an array with the largest negative integer and `null`.

If there are both negative and positive integers, it returns an array with the largest negative integer and the smallest positive integer.

The `Math.max` and `Math.min` functions are used to find the largest and smallest integers, respectively. The spread operator `...` is used to convert the arrays of integers into arguments for these functions. 