  let count = 0;
  for (let i = 1; i < n; i++) {
    for (let j = i + 1; j < n; j++) {
      for (let k = j + 1; k <= n; k++) {
        if ((i * i - i + 1 + j * j - j + 1 + k * k - k + 1) % 3 === 0) {
          count++;
        }
      }
    }
  }
  return count;
}
// More efficient solution
const getMaxTriples = (n) => {
  let count = 0;
  for (let i = 1; i * i - i + 1 <= n; i++) {
    for (let j = i + 1; (i * i - i + 1 + j * j - j + 1) <= n; j++) {
      if ((i * i - i + 1 + j * j - j + 1 + n) % 3 === 0) {
        count++;
      }
    }
  }
  return count;
}