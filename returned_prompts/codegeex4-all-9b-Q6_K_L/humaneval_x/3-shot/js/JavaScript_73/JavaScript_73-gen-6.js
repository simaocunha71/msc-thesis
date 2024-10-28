  var counter = 0;
  for (var i = 0; i < arr.length / 2; i++) {
    if (arr[i] != arr[arr.length - 1 - i]) {
      counter += 1;
    }
  }
  return counter;
}