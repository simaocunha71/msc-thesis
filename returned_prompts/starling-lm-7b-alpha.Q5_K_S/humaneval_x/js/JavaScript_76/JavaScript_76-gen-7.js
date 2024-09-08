  let result = 1;
  let exponent = 0;

  while (result < x) {
    result *= n;
    exponent += 1;
  }

  return exponent == 0 && result == x;
}



