  if (n == 1) {
    return 1;
  }
  if (n == 2) {
    return 2;
  }

  return 9 * Math.pow(10, n - 2) + 9 * Math.pow(10, n - 3);
}



