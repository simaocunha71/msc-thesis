  let result = 1;
  for (let i = 0; i < 31; i++) {
    result = (result * result) % p;
    if (n & (1 << i)) {
      result = (result * p) % p;
    }
  }
  return result;
}



