  var digits = x.toString().split('');
  var length = digits.length;

  if (shift > length) {
    digits = digits.reverse();
  } else {
    digits.push(digits.shift());
  }
  digits.shift();
  return digits.join('');
}



