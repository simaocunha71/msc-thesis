  let digits = x.toString();
  if (shift > digits.length) {
    shift = digits.length - shift;
    digits = digits.split('').reverse().join('');
  }
  digits = digits.slice(shift).concat(digits.slice(0, shift));
  return parseInt(digits);
}



