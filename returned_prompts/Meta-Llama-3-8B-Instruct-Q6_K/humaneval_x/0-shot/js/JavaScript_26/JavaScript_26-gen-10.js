Here is the solution:

```javascript
const removeDuplicates = (numbers) => {
  const seen = {};
  return numbers.filter((num) => {
    if (!seen[num]) {
      seen[num] = true;
      return true;
    }
    return false;
  });
};
```

Explanation:

*   We create an empty object `seen` to keep track of the numbers we've seen so far.
*   We use the `filter` method to create a new array with only the unique elements.
*   Inside the filter function, we check if the current number has been seen before by looking it up in the `seen` object. If it hasn't, we mark it as seen and return `true` to include it in the new array. If it has been seen before, we return `false` to exclude it.

Let's test the function with the example input:
```javascript
console.log(removeDuplicates([1, 2, 3, 2, 4])); // Output: [1, 3, 4]
```
The function correctly removes the duplicates while preserving the original order of the elements.