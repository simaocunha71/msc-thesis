  let result = "";
  let quotient = x;
  while (quotient >= 1) {
    let remainder = quotient % base;
    let char = String.fromCharCode(48 + remainder);
    result = char + result;
    quotient = Math.floor(quotient / base);
  }

  return result;
}



