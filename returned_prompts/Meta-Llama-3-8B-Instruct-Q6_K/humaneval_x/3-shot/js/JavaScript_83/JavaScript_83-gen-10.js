  let count = 0;
  for (let i = 1; i < 10; i++) {
    if (i == 1 || i == Math.pow(10, n - 1) % 10) {
      count++;
    }
  }
  return count;
}