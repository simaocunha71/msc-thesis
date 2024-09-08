  if (n <= 0) {
    return 0;
  } else if (n == 1) {
    return 2;
  } else {
    return 10 * (startsOneEnds(n - 1)) + 9;
  }
}



