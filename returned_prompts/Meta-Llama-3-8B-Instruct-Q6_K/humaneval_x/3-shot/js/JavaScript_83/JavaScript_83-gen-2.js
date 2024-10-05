  let count = 0;
  for (let i = 1; i < 10; i++) {
    if (i == 1 || i % 10 == 1) {
      count += Math.pow(10, n - 1);
    }
  }
  for (let i = 1; i < 10; i++) {
    if (i == 1 || i % 10 == 1) {
      count += Math.pow(10, n - 1) * (i - 1);
    }
  }
  return count;
}



