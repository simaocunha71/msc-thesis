  let sum = array[0] + array[array.length - 1];
  let copyArray = array.slice();
  if (sum % 2 === 0) {
    copyArray.sort((a, b) => b - a);
  } else {
    copyArray.sort((a, b) => a - b);
  }
  return copyArray;
}