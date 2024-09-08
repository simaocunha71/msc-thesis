  if (x % 2 == 0 && y % 2 == 0) {
    if (x == y) {
      return x;
    } else if (x > y) {
      return y;
    } else {
      return x;
    }
  } else if (x % 2 == 0) {
    return x;
  } else if (y % 2 == 0) {
    return y;
  } else {
    return -1;
  }
}



