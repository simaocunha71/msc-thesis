  let result = 1;
  let base = n;
  while (p > 0) {
    if (p % 2 == 1) {
      result = (result * base) % n;
    }
    base = (base * base) % n;
    p = Math.floor(p / 2);
  }
  return result;
}



