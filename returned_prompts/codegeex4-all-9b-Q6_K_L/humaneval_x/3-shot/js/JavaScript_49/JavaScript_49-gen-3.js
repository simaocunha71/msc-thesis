  let result = 1;
  for (let i = 0; i < n; i++) {
    result = (result * 2) % p;
  }
  return result;
}



