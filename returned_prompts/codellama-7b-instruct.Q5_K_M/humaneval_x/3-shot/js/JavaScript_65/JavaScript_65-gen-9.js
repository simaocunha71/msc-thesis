  var digits = x.toString().split('').map(Number);
  shift = shift % digits.length;
  var result = digits.slice(shift).concat(digits.slice(0, shift));
  return result.join('');
}



