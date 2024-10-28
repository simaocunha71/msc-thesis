  let count = 0;
  for (let i = 1; i < 10; i++) {
    count += Math.pow(10, n - 1);
  }
  for (let i = 1; i < 10; i++) {
    count += Math.pow(9, n - 1) + 1;
  }
  return count;
} 



