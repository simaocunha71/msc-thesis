  if (n % 2 !== 0 || n < 8) {
    return false;
  }

  for (let i = 0; i < n; i += 2) {
    for (let j = i + 2; j < n; j += 2) {
      for (let k = j + 2; k < n; k += 2) {
        for (let l = k + 2; l < n; l += 2) {
          if (i + j + k + l === n) {
            return true;
          }
        }
      }
    }
  }

  return false;
}