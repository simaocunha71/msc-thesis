  var smallest = Infinity;
  var index = -1;

  for (var i = 0; i < arr.length; i++) {
    if (arr[i] % 2 == 0) {
      if (arr[i] < smallest) {
        smallest = arr[i];
        index = i;
      }
    }
  }

  return [smallest, index];
}