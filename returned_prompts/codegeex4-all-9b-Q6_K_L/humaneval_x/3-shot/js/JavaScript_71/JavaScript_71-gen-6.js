  if (a + b > c && a + c > b && b + c > a) {
    return ((a + b + c) / 2) * ((a + b + c) / 2 - a) * ((a + b + c) / 2 - b) * ((a + b + c) / 2 - c);
  } else {
    return -1;
  }
}