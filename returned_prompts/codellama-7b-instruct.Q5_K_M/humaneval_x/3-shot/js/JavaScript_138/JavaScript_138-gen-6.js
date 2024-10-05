  if (n < 8) return false;

  for (let i = 2; i <= n; i += 2) {
    if (n == i + i + i + i) {
      return true;
    }
  }

  return false;
}



