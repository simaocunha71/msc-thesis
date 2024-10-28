  const sum = array[0] + array[array.length - 1];
  if (sum % 2 == 0) {
    array.sort((a, b) => b - a);
  } else {
    array.sort((a, b) => a - b);
  }
  return array;
}



