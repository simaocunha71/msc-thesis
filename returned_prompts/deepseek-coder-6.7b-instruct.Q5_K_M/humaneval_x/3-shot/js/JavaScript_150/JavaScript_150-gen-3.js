  if (n < 2) {
    return y;
  }
  for (let i = 2; i * i <= n; i++) {
    if (n % i === 0) {
      return y;
    }
  }
  return x;
}



