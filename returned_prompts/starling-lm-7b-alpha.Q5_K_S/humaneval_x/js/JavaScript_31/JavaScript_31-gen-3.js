  if (n < 2) {
    return false;
  }
  if (n == 2 || n == 3) {
    return true;
  }
  if (n % 2 == 0) {
    return false;
  }
  if (n % 3 == 0) {
    return false;
  }
  let i = 5;
  while (i * i <= n) {
    if (n % i === 0) {
      return false;
    }
    if (n % (i + 2) === 0) {
      return false;
    }
    i += 6;
  }
  return true;
}


