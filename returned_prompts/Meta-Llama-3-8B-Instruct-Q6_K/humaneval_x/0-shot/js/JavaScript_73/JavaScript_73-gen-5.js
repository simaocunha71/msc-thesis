Here is the solution using a two-pointer approach:

```javascript
const smallestChange = (arr) => {
  let left = 0, right = arr.length - 1, changes = 0;
  while (left < right) {
    if (arr[left] !== arr[right]) {
      changes++;
      let min = Math.min(arr[left], arr[right]);
      let max = Math.max(arr[left], arr[right]);
      for (let i = left; i <= right; i++) {
        if (arr[i] === min) {
          arr[i] = max;
          break;
        }
      }
    }
    left++;
    right--;
  }
  return changes;
};
```

The idea is to start from the beginning and end of the array, and move towards the center. If the elements at the two pointers are not equal, we change the smaller element to the larger one. We keep track of the number of changes made. If the array is already palindromic, the number of changes will be 0.

For example, for the array [1,2,3,5,4,7,9,6], we can change the 3 to 4, the 5 to 4, the 7 to 6, and the 9 to 6, resulting in the palindromic array [1,2,4,4,4,6,6,6]. The number of changes is 4.

The time complexity is O(n), where n is the length of the array, and the space complexity is O(1), since we only use a constant amount of space to store the pointers and the changes.