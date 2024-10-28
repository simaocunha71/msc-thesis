  const copyArray = array.slice();
  const sum = array[0] + array[array.length - 1];
  return copyArray.sort((a, b) => (sum % 2 === 0 ? b - a : a - b));
}



