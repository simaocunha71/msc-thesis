  let left = 0;
  let right = arr.length - 1;
  let count = 0;
  while (left < right) {
    if (arr[left] !== arr[right]) {
      count++;
    }
    left++;
    right--;
  }
  return count;
}



