Here is a JavaScript solution for the problem:

```javascript
const largestSmallestIntegers = (lst) => {
  if (lst.length === 0) return [null, null];

  const negative = lst.filter(num => num < 0);
  const positive = lst.filter(num => num > 0);

  if (negative.length > 0) {
    const largestNegative = Math.max(...negative);
    return [largestNegative, positive.length > 0 ? Math.min(...positive) : null];
  } else if (positive.length > 0) {
    return [null, Math.min(...positive)];
  } else {
    return [null, null];
  }
};
```
This function first checks if the input list is empty. If it is, it returns a list with two null values.

Then, it filters the list to get the negative and positive integers separately.

If there are negative integers, it finds the largest one and returns a list with that value and the smallest positive integer (or null if there are no positive integers).

If there are no negative integers but positive integers, it finds the smallest positive integer and returns a list with null and that value.

If there are no integers at all, it returns a list with two null values.