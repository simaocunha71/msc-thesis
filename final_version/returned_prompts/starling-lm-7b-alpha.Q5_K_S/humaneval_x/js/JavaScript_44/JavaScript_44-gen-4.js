  let result = '';

  while (x > 0) {
    let remainder = x % base;
    result += String(remainder);
    x = Math.floor(x / base);
  }

  return result;
}



