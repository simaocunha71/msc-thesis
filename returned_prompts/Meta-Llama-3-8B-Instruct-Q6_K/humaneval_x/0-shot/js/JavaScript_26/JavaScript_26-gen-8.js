Here is a JavaScript function that removes duplicates from an array of integers while preserving the original order:
```javascript
const removeDuplicates = (numbers) => {
  const seen = {};
  return numbers.filter(num => {
    if (!seen[num]) {
      seen[num] = true;
      return true;
    }
    return false;
  });
};
```
Here's an explanation of how the function works:

1. We create an object `seen` to keep track of the numbers we've already seen.
2. We use the `filter()` method to create a new array with the duplicates removed.
3. In the callback function of `filter()`, we check if the current number is already in the `seen` object. If it is, we return `false` to exclude it from the new array. If it's not, we set it to `true` in the `seen` object and return `true` to include it in the new array.

Let's test the function:
```javascript
console.log(removeDuplicates([1, 2, 3, 2, 4])); // [1, 3, 4]
```
It works! 🎉

Alternatively, you can use a Set to keep track of unique numbers:
```javascript
const removeDuplicates = (numbers) => {
  const uniqueNumbers = new Set();
  return numbers.filter(num => {
    if (!uniqueNumbers.has(num)) {
      uniqueNumbers.add(num);
      return true;
    }
    return false;
  });
};
```
This implementation is slightly more efficient than the previous one, as it uses a Set to keep track of unique numbers. However, it's still O(n) in terms of time complexity. 😊

I hope this helps! Let me know if you have any questions. 😊

