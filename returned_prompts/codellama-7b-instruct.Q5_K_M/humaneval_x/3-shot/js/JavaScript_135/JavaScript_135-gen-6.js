  var last = arr[arr.length - 1];
  for (var i = arr.length - 2; i >= 0; i--) {
    if (arr[i] <= last) {
      last = arr[i];
    } else {
      return i;
    }
  }
  return -1;
}



