  var max = arr[0];
  var max_index = 0;

  for (let i = 1; i < arr.length; i++) {
    if (arr[i] <= max) {
      return i - 1;
    }
    if (arr[i] > max) {
      max = arr[i];
      max_index = i;
    }
  }
  return -1;
}