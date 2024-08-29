  let digits = [];
  while (x > 0) {
    digits.unshift(x % base);
    x = Math.floor(x / base);
  }
  return digits.join('');
}



