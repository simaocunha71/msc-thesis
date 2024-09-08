  let largest_index = 0;
  for (let i = 1; i < arr.length; i++) {
    if (arr[i] > arr[i - 1]) {
      largest_index = -1;
      break;
    } else if (arr[i] < arr[i - 1]) {
      largest_index = i;
    }
  }

  return largest_index;
}



