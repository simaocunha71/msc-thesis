  let num = parseFloat(value);
  let intPart = Math.floor(num);
  let decimalPart = num - intPart;

  if (decimalPart < 0.5) {
    return intPart;
  } else {
    return intPart + 1;
  }
}