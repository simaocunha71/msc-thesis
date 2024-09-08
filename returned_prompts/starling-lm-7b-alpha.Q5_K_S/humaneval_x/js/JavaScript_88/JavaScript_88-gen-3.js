  let first = array[0];
  let last = array[array.length - 1];
  let sum = first + last;

  if (sum % 2 === 0) {
    return array.sort((a, b) => b - a);
  } else {
    return array.sort((a, b) => a - b);
  }
}



