  let count = 0;
  for (let i = 1; i <= Math.pow(10, n) - 1; i++) {
    if (i % 10 == 1 || i / 10 % 1 == 1) {
      count += 1;
    }
  }
  return count;
}



