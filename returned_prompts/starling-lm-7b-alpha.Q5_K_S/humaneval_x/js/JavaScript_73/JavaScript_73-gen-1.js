  const arrLength = arr.length;
  let result = 0;
  let left = 0;
  let right = arrLength - 1;
  while (left <= right) {
    if (arr[left] != arr[right]) {
      result += 1;
      const min = Math.min(arr[left], arr[right]);
      for (let i = left + 1; i < right; i++) {
        if (arr[i] == min) {
          arr[i] += 1;
        }
      }
    }
    left += 1;
    right -= 1;
  }
  return result;
}



