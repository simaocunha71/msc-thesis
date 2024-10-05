Here's one way you can solve this problem:

```javascript
const smallestChange = (arr) => {
  let left = 0;
  let right = arr.length - 1;
  let changes = 0;

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

This solution works by using two pointers, `left` and `right`, starting from the beginning and end of the array respectively. If the values at these pointers are not equal, it means we need to make a change to make the array palindromic, so we increment `changes` by one.

After each comparison, we move the pointers towards the center of the array by incrementing `left` and decrementing `right`. We continue this process until `left` is greater than or equal to `right`, which means we have checked all elements in the array.

Finally, we return `changes`, which represents the minimum number of elements that need to be changed to make the array palindromic.