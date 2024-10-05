  let count = 0;
  let start = 0;
  let end = arr.length - 1;

  while (start < end) {
    if (arr[start] != arr[end]) {
      count += 1;
      if (arr[start] > arr[end]) {
        arr[start] -= 1;
      } else {
        arr[end] -= 1;
      }
    }
    start += 1;
    end -= 1;
  }

  return count;
}