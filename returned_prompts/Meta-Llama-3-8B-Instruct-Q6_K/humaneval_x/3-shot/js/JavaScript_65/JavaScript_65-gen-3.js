  let digits = x.toString().split('');
  shift = shift % digits.length;
  if (shift === 0) return x.toString();
  return digits.slice(shift).concat(digits.slice(0, shift)).join('');
}