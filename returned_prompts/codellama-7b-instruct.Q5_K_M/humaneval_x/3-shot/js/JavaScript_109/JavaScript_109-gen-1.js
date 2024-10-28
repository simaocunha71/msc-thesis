  arr.sort((a, b) => a - b);
  var i = arr.length;
  while (i > 0) {
    var j = i - 1;
    while (arr[j] === arr[j - 1]) {
      j--;
    }
    if (j === 0) {
      return true;
    }
    i = j;
  }
  return false;
}



