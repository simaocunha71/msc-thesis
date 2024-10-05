  let count = 0;
  for (let i = 1; i < n; i++) {
    for (let j = i + 1; j < n; j++) {
      for (let k = j + 1; k <= n; k++) {
        let sum = (i * i - i + 1) + (j * j - j + 1) + (k * k - k + 1);
        if (sum % 3 === 0) {
          count++;
        }
      }
    }
  }
  return count;
}