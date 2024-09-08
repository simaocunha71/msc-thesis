  let result = [];
  let i = 2;
  while (i * i <= n) {
    while (n % i == 0) {
      n /= i;
      if (result.indexOf(i) == -1) {
        result.push(i);
      }
    }
    i += 1;
  }
  if (n != 1) {
    result.push(n);
  }
  return result;
}



