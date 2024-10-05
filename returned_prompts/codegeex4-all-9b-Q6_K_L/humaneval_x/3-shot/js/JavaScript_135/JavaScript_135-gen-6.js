  var largest = -1;

  for (var i = 1; i < arr.length; i++) {
    if (arr[i] < arr[i-1]) {
      largest = i;
    }
  }

  return largest;
}



