  let sum = 0;
  for (const n of lst) {
    if (n % 1 === 0 && n >= 0 && n % 2 === 1) {
      sum += Math.pow(n, 2);
    }
  }
  return sum;
}



