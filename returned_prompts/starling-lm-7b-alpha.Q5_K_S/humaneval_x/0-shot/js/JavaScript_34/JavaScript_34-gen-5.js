To solve this problem, we can follow these steps:

1. Create an empty array called "seen" to store the unique elements we've encountered so far.
2. Create a variable called "result" to store the sorted unique elements.
3. Iterate through the input list "l".
4. For each element in the list, check if it's already in the "seen" array. If not, add it to the "seen" array and push it to the "result" array.
5. After the iteration, sort the "result" array in ascending order.
6. Return the sorted "result" array.

Here's the code implementation:

```javascript
const unique = (l) => {
  let seen = [];
  let result = [];

  for (let i = 0; i < l.length; i++) {
    if (!seen.includes(l[i])) {
      seen.push(l[i]);
      result.push(l[i]);
    }
  }

  result.sort((a, b) => a - b);

  return result;
};
```

You can test the function with the provided input:

```javascript
console.log(unique([5, 3, 5, 2, 3, 3, 9, 0, 123])); // [0, 2, 3, 5, 9, 123]
```

The function will return the sorted unique elements in the input list, which in this case is `[0, 2, 3, 5, 9, 123]`.

The function works by iterating through the input list and keeping track of the unique elements encountered using the "seen" array. If an element is not in the "seen" array, it is added to both the "seen" and "result" arrays. Finally, the "result" array is sorted in ascending order and returned.

This approach ensures that only the first occurrence of each element is included in the result, effectively eliminating duplicates.

By sorting the "result" array at the end, the function provides the unique elements in ascending order, which was specified in the original problem statement.

Overall,