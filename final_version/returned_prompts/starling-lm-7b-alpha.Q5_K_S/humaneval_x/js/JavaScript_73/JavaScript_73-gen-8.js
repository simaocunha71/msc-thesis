  let count = 0;
  let left = 0;
  let right = arr.length - 1;

  while (left < right) {
    if (arr[left] != arr[right]) {
      let min = Math.min(arr[left], arr[right]);
      let max = Math.max(arr[left], arr[right]);
      if (max % 2 == 0) {
        if (arr[left] % 2 == 0) {
          arr[left] = min;
          arr[right] = min;
          count += 2;
        } else {
          arr[left] = max;
          arr[right] = max;
          count += 2;
        }
      } else {
        if (arr[left] % 2 != 0) {
          arr[left] = min;
          arr[right] = min;
          count += 2;
        } else {
          arr[left] = max;
          arr[right] = max;
          count += 2;
        }
      }
    }
    left++;
    right--;
  }

  return count;
}



