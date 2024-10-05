  if (arr.length == 0) {
    return true;
  }

  let min = arr[0];
  let min_index = 0;

  for (let i = 1; i < arr.length; i++) {
    if (arr[i] < min) {
      min = arr[i];
      min_index = i;
    }
  }

  if (min_index == 0) {
    return true;
  }

  for (let i = 0; i < arr.length; i++) {
    if (i < min_index) {
      if (arr[i] > min) {
        return false;
      }
    }
  }

  return true;
}