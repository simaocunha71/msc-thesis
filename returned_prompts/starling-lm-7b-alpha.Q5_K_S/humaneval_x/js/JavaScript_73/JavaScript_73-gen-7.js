  let left = 0;
  let right = arr.length - 1;

  let result = 0;
  while (left < right) {
    if (arr[left] != arr[right]) {
      result += 1;
    }
    left += 1;
    right -= 1;
  }

  return result;
}



