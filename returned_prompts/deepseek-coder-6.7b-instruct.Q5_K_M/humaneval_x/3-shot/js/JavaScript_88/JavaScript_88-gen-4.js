  const copy = array.slice();
  const sum = array[0] + array[array.length - 1];
  return copy.sort((a, b) => (sum % 2 === 0 ? b - a : a - b));
}



