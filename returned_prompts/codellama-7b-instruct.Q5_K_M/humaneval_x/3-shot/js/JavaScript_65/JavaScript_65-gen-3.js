  var digits = x.toString().split('');
  if (shift >= digits.length) {
    digits.reverse();
  } else {
    digits = digits.slice(shift).concat(digits.slice(0, shift));
  }
  return digits.join('');
}



