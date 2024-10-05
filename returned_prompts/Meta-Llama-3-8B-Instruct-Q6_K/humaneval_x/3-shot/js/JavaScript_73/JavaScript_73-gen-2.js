  let left = 0;
  let right = arr.length - 1;
  let changes = 0;

  while (left < right) {
    if (arr[left] !== arr[right]) {
      changes++;
      left++;
      right--;
    } else {
      left++;
      right--;
    }
  }

  return changes;
}
// The time complexity is O(n), where n is the length of the array. This is because we are traversing the array once. The space complexity is O(1), as we are using a constant amount of space to store the left and right pointers, and the changes counter.