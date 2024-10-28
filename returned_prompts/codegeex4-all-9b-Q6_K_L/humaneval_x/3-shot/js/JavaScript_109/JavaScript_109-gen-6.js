  if (arr.length == 0) return true;

  let min = arr[0];
  let min_index = 0;
  let max = arr[0];
  let max_index = 0;

  for (let i = 0; i < arr.length; i++) {
    if (arr[i] < min) {
      min = arr[i];
      min_index = i;
    }
    if (arr[i] > max) {
      max = arr[i];
      max_index = i;
    }
  }

  if (min_index > max_index) {
    return true;
  } else {
    return false;
  }
}