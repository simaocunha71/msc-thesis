  let digits = x.toString().split('');
  if (shift >= digits.length) {
    return digits.reverse().join('');
  } else {
    let result = [];
    for (let i = shift; i < digits.length; i++) {
      result.push(digits[i]);
    }
    for (let i = 0; i < shift; i++) {
      result.push(digits[i]);
    }
    return result.join('');
  }
} 