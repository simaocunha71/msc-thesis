  let factor = 2;
  while (factor * factor <= n) {
    if (n % factor !== 0) {
      factor += 1;
    } else {
      n /= factor;
    }
  }
  return n;
}



