  let count = 0;
  for (const n of arr) {
    let sum = 0;
    while (n > 0) {
      sum += (n % 10);
      n = Math.floor(n / 10);
    }
    if (sum > 0) {
      count += 1;
    }
  }

  return count;
}



