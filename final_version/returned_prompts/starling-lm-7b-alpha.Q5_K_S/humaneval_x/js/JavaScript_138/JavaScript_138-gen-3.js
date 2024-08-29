  for (let i = 2; i <= n; i += 2) {
    if (n - i == 0) {
      return true;
    }
    for (let j = 2; j < i; j += 2) {
      if (i + j + (n - i - j) == n && i + j <= n && n - i - j >= 0) {
        return true;
      }
    }
  }
  return false;
}



