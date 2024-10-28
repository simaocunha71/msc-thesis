  if (x > y) {
    return -1;
  }

  if (x % 2 == 0) {
    return x;
  } else if (y % 2 == 0) {
    return y;
  } else {
    return x + 1;
  }
}