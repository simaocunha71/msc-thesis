  let sortedArray = array.slice();
  let first = array[0];
  let last = array[array.length - 1];

  if ((first + last) % 2 == 0) {
    sortedArray.sort((a, b) => b - a);
  } else {
    sortedArray.sort((a, b) => a - b);
  }

  return sortedArray;
};



