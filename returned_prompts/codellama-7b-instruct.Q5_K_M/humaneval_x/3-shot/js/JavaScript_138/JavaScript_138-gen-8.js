  for (let i = 2; i <= n; i += 2) {
    if (n % i == 0) {
      let remaining = n - i;
      if (remaining % 2 == 0) {
        return true;
      }
    }
  }
  return false;
}



