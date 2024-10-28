  var sum = array[0] + array[array.length - 1];
  var copy = array.slice(0);
  if (sum % 2 == 0) {
    copy.sort((a, b) => b - a);
  } else {
    copy.sort((a, b) => a - b);
  }
  return copy;
}