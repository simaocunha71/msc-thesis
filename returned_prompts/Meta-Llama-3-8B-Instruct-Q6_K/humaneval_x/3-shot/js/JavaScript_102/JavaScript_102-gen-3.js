  if (x % 2 == 0) {
    return Math.max(x, y);
  } else if (y % 2 == 0) {
    return y;
  } else {
    return -1;
  }
}
