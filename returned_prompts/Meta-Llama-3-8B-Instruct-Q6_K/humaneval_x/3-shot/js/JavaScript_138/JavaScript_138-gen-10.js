  for (let i = 2; i < n; i++) {
    if (n - i % 2 === 0) {
      let sum = 0;
      for (let j = 2; j <= i; j++) {
        if (j % 2 === 0) {
          sum += j;
        }
      }
      if (sum === n) {
        return true;
      }
    }
  }
  return false;
}