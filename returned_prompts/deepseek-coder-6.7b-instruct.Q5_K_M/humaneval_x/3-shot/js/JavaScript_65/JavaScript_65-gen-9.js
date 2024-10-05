  let digits = String(x).split('');
  let size = digits.length;
  if (shift >= size) {
    return digits.reverse().join('');
  }
  let shifted = digits.splice(size - shift, shift).concat(digits);
  return shifted.join('');
}



