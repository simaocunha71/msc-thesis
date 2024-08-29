  if (n == 1) {
    return x == 1;
  }
  while (x % n == 0) {
    x /= n;
  }
  return x == 1;
}



