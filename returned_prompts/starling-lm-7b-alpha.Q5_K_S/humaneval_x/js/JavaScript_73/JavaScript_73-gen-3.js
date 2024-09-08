  let left = 0;
  let right = arr.length - 1;
  let count = 0;
  while (left < right) {
    if (arr[left] != arr[right]) {
      if (arr[left] == arr[right] + 1) {
        arr[right] = arr[left];
      } else if (arr[left] + 1 == arr[right]) {
        arr[left] = arr[right];
      } else {
        count += 1;
        if (arr[left] < arr[right]) {
          arr[right] = arr[left];
        } else {
          arr[left] = arr[right];
        }
      }
    }
    left += 1;
    right -= 1;
  }
  return count;
}



