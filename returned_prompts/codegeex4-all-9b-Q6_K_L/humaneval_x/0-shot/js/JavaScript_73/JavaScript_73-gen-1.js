The problem can be solved by comparing the elements from the start and end of the array, and keeping track of the number of changes needed. If the elements are not equal, we increment a counter and replace the element with the other one. Finally, we return the counter as the minimum number of changes needed.

Here is the implementation in JavaScript:

```javascript
const smallestChange = (arr) => {
  let changes = 0;
  let start = 0;
  let end = arr.length - 1;

  while (start < end) {
    if (arr[start] !== arr[end]) {
      changes++;
      arr[start] = arr[end];
    }
    start++;
    end--;
  }

  return changes;
};

console.log(smallestChange([1, 2, 3, 5, 4, 7, 9, 6])); // 4
console.log(smallestChange([1, 2, 3, 4, 3, 2, 2])); // 1
console.log(smallestChange([1, 2, 3, 2, 1])); // 0
```

This solution has a time complexity of O(n), where n is the length of the array.