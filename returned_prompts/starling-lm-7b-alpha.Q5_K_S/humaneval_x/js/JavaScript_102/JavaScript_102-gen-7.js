  if (x % 2 != 0) {
    x -= 1;
  }
  if (y % 2 != 0) {
    y -= 1;
  }
  if (x <= y) {
    if (y % 2 == 0) {
      return y;
    } else {
      return x;
    }
  } else {
    return -1;
  }
}



