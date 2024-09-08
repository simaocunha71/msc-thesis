  let max_index = 0;
  for (let i = 1; i < arr.length; i++) {
    if (arr[i] > arr[i - 1]) {
      if (i > max_index) {
        max_index = i;
      }
    } else {
      max_index = Math.max(max_index, i);
    }
  }
  return max_index;
}



