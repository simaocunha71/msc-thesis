You can use the `Array.prototype.filter()` method to get the negative and positive numbers separately, and then use `Array.prototype.sort()` to sort them. Finally, return the last negative number and the first positive number.

Here's how you can implement it:

```javascript
const largestSmallestIntegers = (lst) => {
  let negatives = lst.filter(num => num < 0).sort((a, b) => b - a);
  let positives = lst.filter(num => num > 0).sort((a, b) => a - b);
  
  return [
    negatives.length === 0 ? null : negatives[0],
    positives.length === 0 ? null : positives[0]
  ];
}
```

In this code:

- `lst.filter(num => num < 0)` returns a new array with all the negative numbers.
- `.sort((a, b) => b - a)` sorts the negative numbers in descending order.
- `lst.filter(num => num > 0)` returns a new array with all the positive numbers.
- `.sort((a, b) => a - b)` sorts the positive numbers in ascending order.
- `[negatives.length === 0 ? null : negatives[0], positives.length === 0 ? null : positives[0]]` returns an array with the largest negative number and the smallest positive number. If there are no negative or positive numbers, it returns `null`.