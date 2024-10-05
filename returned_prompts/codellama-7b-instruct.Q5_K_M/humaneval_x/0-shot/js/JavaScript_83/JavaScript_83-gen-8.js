  let count = 0;
  for (let i = 1; i <= 9; i++) {
    if (i === 1 || i === 9) {
      count += Math.pow(9, n - 1);
    }
  }
  return count;
}