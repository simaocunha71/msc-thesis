  let result = 0;
  const a = [];
  for (let i = 1; i <= n; i++) {
    a[i] = i * i - i + 1;
  }

  for (let i = 1; i <= n; i++) {
    for (let j = i + 1; j <= n; j++) {
      for (let k = j + 1; k <= n; k++) {
        if ((a[i] + a[j] + a[k]) % 3 === 0) {
          result += 1;
        }
      }
    }
  }

  return result;
}


