  var digits = x.toString().split('');
  if (shift > digits.length) {
    return digits.reverse().join('');
  }

  var shifted_digits = digits.slice(shift);
  shifted_digits = shifted_digits.concat(digits.slice(0, shift));
  return shifted_digits.join('');
}



