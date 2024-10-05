  let digits = x.toString().split('');
  shift = shift % digits.length;
  if (shift === 0) {
    return x.toString();
  }
  return digits.splice(digits.length - shift, shift).concat(digits).join('');
}