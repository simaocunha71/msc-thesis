  if (n == 1) {
    return 2;
  } else {
    return startsOneEnds(n - 1) * 2;
  }
}