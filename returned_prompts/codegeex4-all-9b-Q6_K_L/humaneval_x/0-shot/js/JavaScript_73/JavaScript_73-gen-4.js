To solve this problem, you can use a two-pointer approach. Start with two pointers, one at the beginning of the array and the other at the end. Compare the elements at these two pointers. If they are not equal, increment the count of changes and move the pointer that points to the element that is larger towards the middle of the array. Continue this process until the two pointers meet or cross each other. The count of changes will give you the minimum number of elements that need to be changed to make the array palindromic.

Here's the implementation in JavaScript:

```javascript
const smallestChange = (arr) => {
  let count = 0;
  let left = 0;
  let right = arr.length - 1;

  while (left < right) {
    if (arr[left] !== arr[right]) {
      count++;
    }
    left++;
    right--;
  }

  return count;
};

console.log(smallestChange([1, 2, 3, 5, 4, 7, 9, 6])); // 4
console.log(smallestChange([1, 2, 3, 4, 3, 2, 2])); // 1
console.log(smallestChange([1, 2, 3, 2, 1])); // 0
```

The time complexity of this solution is O(n), where n is the length of the array.