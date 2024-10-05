Here is the solution to the problem:

```javascript
const smallestChange = (arr) => {
  const n = arr.length;
  let left = 0, right = n - 1, changes = 0;

  while (left < right) {
    if (arr[left] !== arr[right]) {
      changes++;
    }
    left++;
    right--;
  }

  return changes;
};
```

This function works by comparing elements from the start and end of the array and counting the number of mismatches. If two elements are not equal, we increment the `changes` counter. We continue this process until the start and end indices meet in the middle of the array. The `changes` counter will hold the minimum number of elements that need to be changed to make the array palindromic.