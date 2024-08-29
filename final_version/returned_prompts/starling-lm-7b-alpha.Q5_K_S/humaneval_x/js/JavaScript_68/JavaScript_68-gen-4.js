  let min = Number.MAX_SAFE_INTEGER;
  let minIndex = -1;
  for (let i = 0; i < arr.length; i++) {
    const value = arr[i];
    if (value % 2 == 0 && value < min) {
      min = value;
      minIndex = i;
    }
  }
  return minIndex == -1 ? [] : [min, minIndex];
}



