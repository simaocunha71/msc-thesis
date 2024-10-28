  if (n == 1) {
    return 1;
  }

  for (let i = n / 2; i >= 1; i--) {
    if (n % i == 0) {
      return i;
    }
  }
  return 1;
}



