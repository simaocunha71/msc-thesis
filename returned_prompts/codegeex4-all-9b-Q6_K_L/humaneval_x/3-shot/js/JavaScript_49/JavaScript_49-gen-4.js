  let result = 1;
  for (let i = 0; i < n; i++) {
    result *= 2;
    result %= p;
  }
  return result;
}



