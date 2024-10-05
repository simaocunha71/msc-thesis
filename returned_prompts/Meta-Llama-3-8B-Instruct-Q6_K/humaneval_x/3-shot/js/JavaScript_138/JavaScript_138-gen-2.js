  for (let i = 2; i <= n; i += 2) {
    let sum = 0;
    for (let j = 2; j <= n; j += 2) {
      sum += j;
      if (sum == n) {
        return true;
      } else if (sum > n) {
        break;
      }
    }
  }
  return false;
}
