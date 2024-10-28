  const gcd = (a, b) => {
    if (a % b === 0) {
      return b;
    }
    return gcd(b, a % b);
  };

  return gcd(a, b);

}