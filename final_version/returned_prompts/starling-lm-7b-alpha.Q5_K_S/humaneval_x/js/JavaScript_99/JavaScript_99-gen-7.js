  const number = parseFloat(value);
  if (number % 1.0 === 0) {
    return number;
  }
  const ints = [Math.floor(number), Math.ceil(number)];
  const diff = Math.abs(number - ints[0]);
  const diff2 = Math.abs(number - ints[1]);
  if (diff <= diff2) {
    return ints[0];
  } else {
    return ints[1];
  }
}



