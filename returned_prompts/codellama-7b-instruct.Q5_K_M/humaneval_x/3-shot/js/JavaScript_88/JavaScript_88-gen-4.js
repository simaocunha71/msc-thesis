  var sum = array.slice(0, 1).concat(array.slice(array.length - 1, array.length)).reduce((a, b) => a + b);
  return sum % 2 == 0 ? array.sort((a, b) => b - a) : array.sort((a, b) => a - b);
}



