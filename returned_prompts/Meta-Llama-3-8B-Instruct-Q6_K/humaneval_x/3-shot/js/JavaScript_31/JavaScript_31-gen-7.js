  if (n <= 1) {
    return false;
  }
  if (n === 2) {
    return true;
  }
  if (n % 2 === 0) {
    return false;
  }
  let max_divisor = Math.floor(Math.sqrt(n));
  for (let i = 3; i <= max_divisor; i += 2) {
    if (n % i === 0) {
      return false;
    }
  }
  return true;
}