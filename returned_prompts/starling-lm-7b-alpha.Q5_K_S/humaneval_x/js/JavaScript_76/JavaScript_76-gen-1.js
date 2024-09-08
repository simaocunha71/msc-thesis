  while (x > 1) {
    if (x % n != 0) {
      return false;
    }
    x = Math.floor(x / n);
  }
  return x == 1;
}



