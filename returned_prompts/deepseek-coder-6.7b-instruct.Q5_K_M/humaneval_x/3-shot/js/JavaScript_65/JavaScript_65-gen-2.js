  let digits = String(x).split('');
  if (shift >= digits.length) {
    return digits.reverse().join('');
  } else {
    return digits.splice(-shift).concat(digits).join('');
  }
}



