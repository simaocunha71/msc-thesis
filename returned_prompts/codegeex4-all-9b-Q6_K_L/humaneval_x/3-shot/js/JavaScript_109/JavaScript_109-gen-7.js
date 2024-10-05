  var sorted = arr.sort((a, b) => a - b);
  var first = arr[0];
  var index = 0;
  for (var i = 0; i < arr.length; i++) {
    if (arr[i] === first) {
      index = i;
      break;
    }
  }
  for (var i = 0; i < arr.length; i++) {
    if (arr[i] !== sorted[i]) {
      return false;
    }
  }
  return true;
}