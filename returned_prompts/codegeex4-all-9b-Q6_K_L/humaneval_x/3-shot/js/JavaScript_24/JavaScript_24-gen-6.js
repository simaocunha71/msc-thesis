  for (let i = n - 1; i >= 2; i--) {
    if (n % i == 0) {
      return i;
    }
  }
  return 1;
}



