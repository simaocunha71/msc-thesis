  for (let i = Math.floor(n / 2); i > 0; i--) {
    if (n % i === 0) {
      return i;
    }
  }
  return n;
}



