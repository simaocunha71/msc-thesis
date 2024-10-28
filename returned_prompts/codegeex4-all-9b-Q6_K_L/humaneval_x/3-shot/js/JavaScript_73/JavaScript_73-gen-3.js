  let count = 0;
  let left = 0;
  let right = arr.length - 1;

  while (left < right) {
    if (arr[left] != arr[right]) {
      count += 1;
    }
    left += 1;
    right -= 1;
  }

  return count;
}