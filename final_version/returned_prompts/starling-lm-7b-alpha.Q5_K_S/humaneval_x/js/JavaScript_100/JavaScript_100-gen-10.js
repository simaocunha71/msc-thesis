  let result = [];
  while (n > 0) {
    if (n % 2 === 0) {
      result.push(n);
      n = n - 2;
    } else {
      result.push(n);
      n = n + 1;
    }
  }
  return result;
}



