  let largestIndex = 0;
  for (let i = 1; i < arr.length; i++) {
    if (arr[i] < arr[i-1]) {
      if (i > largestIndex) {
        largestIndex = i;
      }
    }
  }
  return largestIndex;
}



