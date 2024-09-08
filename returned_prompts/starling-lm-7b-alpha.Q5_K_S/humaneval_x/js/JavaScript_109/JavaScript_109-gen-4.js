  let min = Infinity;
  let min_index = 0;
  let isSorted = true;
  for (let i = 0; i < arr.length; i++) {
    if (arr[i] < min) {
      min = arr[i];
      min_index = i;
    }
    if (i > 0 && arr[i] < arr[i - 1]) {
      isSorted = false;
      break;
    }
  }
  return isSorted || (min_index === arr.length - 1);
}



