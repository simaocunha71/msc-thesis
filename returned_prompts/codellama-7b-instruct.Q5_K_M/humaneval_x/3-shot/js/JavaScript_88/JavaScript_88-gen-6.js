  if (array.length == 0) return [];

  let sum = array[0] + array[array.length - 1];
  let result = array.slice().sort((a, b) => a - b);

  if (sum % 2 == 0) {
    return result.reverse();
  } else {
    return result;
  }
}



