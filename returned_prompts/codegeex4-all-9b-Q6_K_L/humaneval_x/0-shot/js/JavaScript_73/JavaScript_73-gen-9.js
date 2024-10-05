To solve this problem, we can follow these steps:

1. Initialize a variable `changeCount` to 0 to keep track of the number of changes needed.
2. Iterate through the array from both ends towards the middle.
3. For each pair of elements at positions `i` and `j` (where `i` starts from 0 and `j` starts from the last index):
   - If the elements are equal, continue to the next pair.
   - If the elements are not equal, increment `changeCount` by 1.
   - If `arr[i]` is less than `arr[j]`, set `arr[j]` to `arr[i]`.
   - If `arr[i]` is greater than `arr[j]`, set `arr[i]` to `arr[j]`.
4. Return `changeCount`.

Here is the implementation of the `smallestChange` function in JavaScript:

```javascript
const smallestChange = (arr) => {
  let changeCount = 0;

  for (let i = 0, j = arr.length - 1; i < j; i++, j--) {
    if (arr[i] !== arr[j]) {
      changeCount++;
      if (arr[i] < arr[j]) {
        arr[j] = arr[i];
      } else {
        arr[i] = arr[j];
      }
    }
  }

  return changeCount;
};
```

Let's test the function with the provided examples:

```javascript
console.log(smallestChange([1, 2, 3, 5, 4, 7, 9, 6])); // Output: 4
console.log(smallestChange([1, 2, 3, 4, 3, 2, 2])); // Output: 1
console.log(smallestChange([1, 2, 3, 2, 1])); // Output: 0
```

The function should return the expected outputs for each example.