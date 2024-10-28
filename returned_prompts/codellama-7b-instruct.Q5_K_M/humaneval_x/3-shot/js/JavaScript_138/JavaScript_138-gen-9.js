  for (let i = 0; i < n; i++) {
    if (i % 2 == 0 && n - i % 2 == 0) {
      if (i + (n - i) == n) {
        return true;
      }
    }
  }
  return false;
}



