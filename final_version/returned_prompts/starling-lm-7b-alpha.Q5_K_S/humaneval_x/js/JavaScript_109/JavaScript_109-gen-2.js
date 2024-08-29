  let max = arr[0];
  let max_index = 0;
  for (let i = 1; i < arr.length; i++) {
    if (arr[i] > max) {
      max = arr[i];
      max_index = i;
    }
  }
  for (let i = 0; i < arr.length; i++) {
    if (arr[i] == max && i != max_index) {
      return false;
    }
  }
  return true;
}



