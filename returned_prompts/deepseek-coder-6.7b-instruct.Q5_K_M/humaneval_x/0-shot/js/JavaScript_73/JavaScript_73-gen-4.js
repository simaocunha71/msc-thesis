  let left = 0, right = arr.length - 1;
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

console.log(smallestChange([1,2,3,5,4,7,9,6])); // 4
console.log(smallestChange([1, 2, 3, 4, 3, 2, 2])); // 1
console.log(smallestChange([1, 2, 3, 2, 1])); // 0
```

This solution works by initializing two pointers, one at the start of the array and the other at the end. It then enters a while loop that continues until the two pointers meet in the middle. In each iteration of the loop, it compares the elements at the current positions of the two pointers. If they are not equal, it increments a counter variable by one. It then moves the left pointer one position to the right and the right pointer one position to the left.

Finally, it returns the count of changes required to make the array palindromic.

This solution has a time complexity of O(n) and a space complexity of O(1), where n is the length of the array.
*/

// 