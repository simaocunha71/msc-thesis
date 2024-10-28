  let sum = array[0] + array[array.length - 1];
  let isOdd = sum % 2 !== 0;
  let sortedArray;

  if (isOdd) {
    sortedArray = array.slice().sort((a, b) => a - b);
  } else {
    sortedArray = array.slice().sort((a, b) => b - a);
  }

  return sortedArray;
}