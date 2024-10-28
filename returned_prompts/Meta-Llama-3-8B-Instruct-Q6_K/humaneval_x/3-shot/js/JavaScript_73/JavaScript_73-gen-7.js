  let left = 0, right = arr.length - 1;
  let count = 0;

  while (left < right) {
    if (arr[left] != arr[right]) {
      count++;
      if (arr[left] < arr[right]) {
        arr[right] = arr[left];
      } else {
        arr[left] = arr[right];
      }
    }
    left++;
    right--;
  }
  return count;
}