  const length = string.length;
  const is_prime = (n) => {
    for (let i = 2; i < n; i++) {
      if (n % i == 0) {
        return false;
      }
    }
    return true;
  }
  return is_prime(length);
}



