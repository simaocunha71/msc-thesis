Here is the solution to the problem:

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

This function uses a hash table (`seen`) to keep track of the numbers that have been seen so far. It then uses the `filter()` method to iterate over the input array. For each number, it checks if the number has been seen before by checking if it exists in the `seen` hash table. If the number has not been seen before, it adds it to the `seen` hash table and returns `true` to include the number in the result array. If the number has been seen before, it returns `false` to exclude the number from the result array. The `filter()` method returns a new array with all the numbers that passed the test implemented by the provided function. In this case, the function returns an array with all the unique numbers from the input array, in the same order as they appeared in the input array.