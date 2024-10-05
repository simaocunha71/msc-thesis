  var sum = array[0] + array[array.length - 1];
  var result = array.slice();
  if (sum % 2 == 0) {
    result.sort((a, b) => b - a);
  } else {
    result.sort((a, b) => a - b);
  }
  return result;
}



