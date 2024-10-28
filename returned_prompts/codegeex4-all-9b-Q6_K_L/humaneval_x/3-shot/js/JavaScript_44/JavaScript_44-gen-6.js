  if (base >= 10 || base <= 1) {
    return "Invalid base";
  }

  let result = '';
  while (x > 0) {
    result = (x % base) + result;
    x = Math.floor(x / base);
  }

  return result;
}