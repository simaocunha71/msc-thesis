  let count = 0;
  for (let i = 2; i < n; i += 2) {
    if (n - i >= 0) {
      n -= i;
      count++;
    }
  }
  return n === 0 && count === 4;
}



