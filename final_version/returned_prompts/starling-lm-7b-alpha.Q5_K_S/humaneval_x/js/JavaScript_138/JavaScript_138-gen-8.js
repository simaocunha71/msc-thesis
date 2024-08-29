  for (let i = 2; i <= n; i += 2) {
    if ((n - i) % 2 === 0) {
      let a = i;
      let b = (n - i) / 2;
      if (a + b === n && a % 2 === 0 && b % 2 === 0) {
        return true;
      }
    }
  }
  return false;
}



