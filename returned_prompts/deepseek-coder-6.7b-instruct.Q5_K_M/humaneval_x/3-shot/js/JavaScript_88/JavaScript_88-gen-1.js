  let sortedArray = [...array];
  let sum = array[0] + array[array.length - 1];
  sortedArray.sort((a, b) => (sum % 2 === 0 ? b - a : a - b));
  return sortedArray;
}



