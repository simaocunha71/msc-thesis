  let count = 0;
  for (let i = 1; i <= n - 2; i++) {
      for (let j = i + 1; j <= n - 1; j++) {
          for (let k = j + 1; k <= n; k++) {
              if ((i * i - i + 1 + j * j - j + 1 + k * k - k + 1) % 3 === 0) {
                  count++;
              }
          }
      }
  }
  return count;
}


