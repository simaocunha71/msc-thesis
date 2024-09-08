  if (x % 2 == 0) {
    if (x == y) {
      return x;
    }
    if (y % 2 == 0) {
      return y;
    }
    return x;
  }
  if (y % 2 == 0) {
    return y;
  }
  return -1;
}



