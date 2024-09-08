  let max = -1;
  for (let i = 0; i < arr.length; i++) {
    if (i == 0) {
      if (arr[i] > arr[i + 1]) {
        return -1;
      }
    } else if (arr[i] > arr[i - 1]) {
      max = i;
    }
  }
  return max;
}



