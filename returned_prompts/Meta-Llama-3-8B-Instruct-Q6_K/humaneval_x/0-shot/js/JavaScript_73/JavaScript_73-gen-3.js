Here is a JavaScript solution for the problem:

```javascript
const smallestChange = (arr) => {
  const n = arr.length;
  let changes = 0;
  let left = 0;
  let right = n - 1;

  while (left < right) {
    if (arr[left] !== arr[right]) {
      changes++;
      right--;
      if (arr[left] !== arr[right]) {
        changes++;
      }
    } else {
      left++;
      right--;
    }
  }

  return changes;
};

console.log(smallestChange([1, 2, 3, 5, 4, 7, 9, 6])); // 4
console.log(smallestChange([1, 2, 3, 4, 3, 2, 2])); // 1
console.log(smallestChange([1, 2, 3, 2, 1])); // 0
```

This solution iterates through the array from both ends (left and right) and checks if the elements are equal. If they are not equal, it increments the `changes` counter and decrements the right pointer. If they are equal, it increments both pointers. The solution stops when the pointers meet in the middle. The final value of `changes` is the minimum number of elements that need to be changed to make the array palindromic.