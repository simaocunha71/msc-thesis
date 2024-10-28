  var min = 1000000;
  var index = 0;
  for (let i = 0; i < arr.length; i++) {
    if (arr[i] % 2 == 0 && arr[i] < min) {
      min = arr[i];
      index = i;
    }
  }
  if (min == 1000000) {
    return [];
  } else {
    return [min, index];
  }
}