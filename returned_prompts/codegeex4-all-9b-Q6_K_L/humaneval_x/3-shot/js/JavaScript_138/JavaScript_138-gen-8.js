  if (n % 2 != 0) {
    return false;
  }

  for (let i = 2; i <= n / 4; i += 2) {
    for (let j = i + 2; j <= n / 3; j += 2) {
      for (let k = j + 2; k <= n / 2; k += 2) {
        let l = n - i - j - k;
        if (l > 0 && l % 2 == 0) {
          return true;
        }
      }
    }
  }

  return false;
}



