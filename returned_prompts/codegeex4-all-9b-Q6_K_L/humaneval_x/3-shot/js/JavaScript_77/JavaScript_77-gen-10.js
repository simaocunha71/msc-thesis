  if (a < 0) {
    a *= -1;
  }
  if (a == 0) {
    return true;
  }
  for (let i = 0; i <= a; i++) {
    if (i * i * i == a) {
      return true;
    }
  }
  return false;
}