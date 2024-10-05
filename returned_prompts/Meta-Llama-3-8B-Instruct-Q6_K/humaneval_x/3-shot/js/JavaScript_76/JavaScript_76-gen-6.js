  for (let i = 2; Math.pow(n, i) <= x; i++) {
    if (Math.pow(n, i) == x) {
      return true;
    }
  }
  return false;
}