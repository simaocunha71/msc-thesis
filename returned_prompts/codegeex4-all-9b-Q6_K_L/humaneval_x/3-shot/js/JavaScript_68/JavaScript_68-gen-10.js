  var smallestEven = [Infinity, -1];
  for (var i = 0; i < arr.length; i++) {
    if (arr[i] % 2 == 0 && arr[i] < smallestEven[0]) {
      smallestEven = [arr[i], i];
    }
  }
  return smallestEven;
}