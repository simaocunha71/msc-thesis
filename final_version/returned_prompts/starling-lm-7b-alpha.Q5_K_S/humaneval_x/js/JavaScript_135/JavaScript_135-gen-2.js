  let max = -1;
  for (let i = 0; i < arr.length; i++) {
    if (arr[i] > max) {
      max = arr[i];
    } else if (arr[i] <= max) {
      if (max == -1) {
        max = arr[i];
      }
    }
  }
  return max;
}



