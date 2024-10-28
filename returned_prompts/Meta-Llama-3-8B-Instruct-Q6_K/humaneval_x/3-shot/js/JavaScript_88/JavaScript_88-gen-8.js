  let sum = array[0] + array[array.length - 1];
  let sortedArray = array.slice();
  if (sum % 2 === 0) {
    sortedArray.sort((a, b) => b - a);
  } else {
    sortedArray.sort((a, b) => a - b);
  }
  return sortedArray;
}