  if (array.length === 0) {
    return array;
  }
  let sum = array[0] + array[array.length - 1];
  let isOdd = sum % 2 !== 0;
  array = array.slice();
  array.sort((a, b) => isOdd ? a - b : b - a);
  return array;
}  // This is the same as `return array.slice().sort(isOdd ? (a, b) => a - b : (a, b) => b - a);`



