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
}...



