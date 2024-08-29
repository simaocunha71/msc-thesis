  let first = array[0];
  let last = array[array.length - 1];

  let isOdd = (first + last) % 2 != 0;

  array.sort((a, b) => {
    return isOdd ? a - b : b - a;
  });

  return array;
}



