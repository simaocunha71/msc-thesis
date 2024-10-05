  var sum = array[0] + array[array.length - 1];
  var sortedArray = [...array].sort((a, b) => sum % 2 == 0 ? a - b : b - a);
  return sortedArray;
}