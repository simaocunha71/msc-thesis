  let digits = x.toString().split('');
  let shifted = digits.splice(digits.length - shift % digits.length, shift % digits.length);
  return digits.join('') + shifted.join('');
}