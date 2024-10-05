  let maxIndex = -1;
  for (let i = 1; i < arr.length; i++) {
    if (arr[i] <= arr[i - 1]) {
      maxIndex = i - 1;
    }
  }
  return maxIndex;
}