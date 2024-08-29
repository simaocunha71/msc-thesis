  let first = array[0];
  let last = array[array.length - 1];
  let result = array.slice();
  let sign = 1;

  if ((first + last) % 2 == 0) {
    sign = -1;
  }

  result.sort((a, b) => a - b * sign);

  return result;
}



