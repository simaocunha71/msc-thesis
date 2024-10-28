You can use a JavaScript Set to remove duplicates from an array. A Set is a collection of unique values, so it automatically removes duplicates when you add elements to it. Here's how you can implement the `removeDuplicates` function using a Set:

```javascript
const removeDuplicates = (numbers) => {
  return [...new Set(numbers)];
};

// Example usage
console.log(removeDuplicates([1, 2, 3, 2, 4])); // Output: [1, 2, 3, 4]
```

In this code, we create a new Set with the `new Set(numbers)` syntax. This will automatically remove any duplicate values from the `numbers` array. Then, we use the spread operator (`...`) to convert the Set back into an array with the `[...new Set(numbers)]` syntax. Finally, we return the resulting array.