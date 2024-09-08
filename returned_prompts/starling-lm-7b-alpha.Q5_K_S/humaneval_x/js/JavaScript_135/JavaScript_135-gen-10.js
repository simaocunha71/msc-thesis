  let maxIndex = -1;

  for (let i = 0; i < arr.length; i++) {
    if (i > maxIndex && arr[i] >= arr[maxIndex]) {
      maxIndex = i;
    }
  }

  return maxIndex;
}



