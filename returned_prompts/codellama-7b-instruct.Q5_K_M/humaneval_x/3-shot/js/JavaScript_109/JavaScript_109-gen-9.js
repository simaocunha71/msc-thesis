  if (arr.length == 0) {
    return true;
  }
  if (arr.length == 1) {
    return true;
  }
  if (arr.length == 2) {
    if (arr[1] > arr[0]) {
      return true;
    } else {
      return false;
    }
  }

  var sorted = false;
  var i = 0;
  while (i < arr.length && !sorted) {
    if (arr[i] > arr[i + 1]) {
      var j = i;
      var k = i + 1;
      while (j >= 0 && k < arr.length) {
        var temp = arr[k];
        arr[k] = arr[j];
        arr[j] = temp;
        j = j - 1;
        k = k + 1;
      }
      sorted = true;
    }
    i = i + 1;
  }
  return sorted;
}



