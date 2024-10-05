  var sum = array[0] + array[array.length - 1];
  if (sum % 2 == 0) {
    return array.slice().sort((a, b) => b - a);
  } else {
    return array.slice().sort((a, b) => a - b);
  }
}