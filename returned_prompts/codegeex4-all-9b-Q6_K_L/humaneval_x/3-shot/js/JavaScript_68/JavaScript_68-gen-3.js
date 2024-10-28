  var smallest = Infinity;
  var smallestIndex = -1;

  for (var i = 0; i < arr.length; i++) {
    if (arr[i] % 2 == 0) {
      if (arr[i] < smallest) {
        smallest = arr[i];
        smallestIndex = i;
      }
    }
  }

  if (smallestIndex == -1) {
    return [];
  } else {
    return [smallest, smallestIndex];
  }
}