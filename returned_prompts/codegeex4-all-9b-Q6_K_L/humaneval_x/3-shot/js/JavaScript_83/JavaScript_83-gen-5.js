  if (n == 1) {
    return 1;
  }
  return 2 * 9 ** (n - 2) + startsOneEnds(n - 1);
}



