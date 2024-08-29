  let max = 0;
  let sum = 0;

  for (const n of lst) {
    if (isPrime(n)) {
      sum += n.toString().split('').reduce((a, b) => a + Number(b), 0);
      max = Math.max(max, n);
    }
  }

  return sum;
}



