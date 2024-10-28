  for (let i = n - 1; i > 0; i--) {
    if (n % i == 0) {
      return i;
    }
  }
  return 1;
} // or return n; for the edge case of n being 1
} // or return 1; for the edge case of n being 1


