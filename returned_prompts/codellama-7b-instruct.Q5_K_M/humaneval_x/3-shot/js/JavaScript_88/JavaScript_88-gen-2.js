  var sum = array[0] + array[array.length - 1];
  if (sum % 2 == 0) {
    return array.sort(function(a, b) {
      return b - a;
    });
  } else {
    return array.sort(function(a, b) {
      return a - b;
    });
  }
}



