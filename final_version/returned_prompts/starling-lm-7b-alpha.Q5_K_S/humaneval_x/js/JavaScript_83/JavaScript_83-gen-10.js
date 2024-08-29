  if (n == 0) {
    return 0;
  }
  if (n == 1) {
    return 2;
  }
  return 10 * startsOneEnds(n - 1) + 9 * startsOneEnds(n - 1);
}



