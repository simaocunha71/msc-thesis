  let digits = Array.from(String(x), Number).reverse();
  if (shift > digits.length) {
    return digits.reverse().join('');
  } else {
    for (let i = 0; i < shift; i++) {
      digits.unshift(digits.pop());
    }
    return digits.join('');
  }
}



