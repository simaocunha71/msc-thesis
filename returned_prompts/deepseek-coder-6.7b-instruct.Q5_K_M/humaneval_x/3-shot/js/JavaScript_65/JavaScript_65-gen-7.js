  let digits = String(x).split('');
  if (shift > digits.length) {
    return digits.reverse().join('');
  } else {
    let shifted = digits.splice(-shift).concat(digits);
    return shifted.join('');
  }
}



