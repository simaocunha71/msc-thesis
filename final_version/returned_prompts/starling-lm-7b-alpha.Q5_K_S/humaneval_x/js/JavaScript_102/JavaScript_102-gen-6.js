  if (x % 2 != 0 && y % 2 != 0) {
    return -1;
  } else if (x % 2 == 0 && y % 2 == 0) {
    if (x >= y) {
      return y;
    } else {
      return x;
    }
  } else if (x % 2 == 0 && y % 2 != 0) {
    return y;
  } else {
    return x;
  }
}



