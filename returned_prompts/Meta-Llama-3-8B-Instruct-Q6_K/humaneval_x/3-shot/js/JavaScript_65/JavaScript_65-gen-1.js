  let digits = x.toString().split('');
  shift = shift % digits.length;
  return digits.slice(shift).concat(digits.slice(0, shift)).join('');
} 