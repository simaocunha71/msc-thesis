  let sum = array[0] + array[array.length - 1];
  let copy = [...array].sort((a, b) => sum % 2 ? a - b : b - a);
  return copy;
}