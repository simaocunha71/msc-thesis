  if (x < 0 || n < 0) {
    return false;
  }

  let power = n;
  while (power <= x) {
    if (power == x) {
      return true;
    }
    power *= n;
  }

  return false;
}



