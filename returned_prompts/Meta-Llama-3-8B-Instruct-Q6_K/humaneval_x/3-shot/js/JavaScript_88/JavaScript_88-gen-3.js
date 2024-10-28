  let sum = array[0] + array[array.length - 1];
  let copy = array.slice();
  if (sum % 2 === 0) {
    copy.sort((a, b) => b - a);
  } else {
    copy.sort((a, b) => a - b);
  }
  return copy;
}