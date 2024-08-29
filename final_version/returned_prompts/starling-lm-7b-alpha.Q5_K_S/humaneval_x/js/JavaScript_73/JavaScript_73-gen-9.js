  let left = 0;
  let right = arr.length - 1;
  let diff_count = 0;
  while (left < right) {
    if (arr[left] !== arr[right]) {
      diff_count += 1;
    }
    left += 1;
    right -= 1;
  }
  return diff_count;
}



