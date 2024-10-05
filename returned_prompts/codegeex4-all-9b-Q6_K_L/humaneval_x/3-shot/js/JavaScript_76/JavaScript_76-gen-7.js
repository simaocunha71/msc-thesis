  let power = 1;
  for (let i = 0; i < x; i++) {
    power *= n;
    if (power == x) {
      return true;
    }
  }
  return false;
}