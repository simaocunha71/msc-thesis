  if (n == 0) {
    return 1;
  }
  if (n % 2 == 0) {
    let half_power = modp(n / 2, p);
    return (half_power * half_power) % p;
  } else {
    return (modp(n - 1, p) * n) % p;
  }
}



