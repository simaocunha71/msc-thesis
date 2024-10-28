  const length = string.length;
  if (length <= 1) {
    return false;
  }
  for (let i = 2, sqrt = Math.sqrt(length); i <= sqrt; i++) {
    if (length % i === 0) {
      return false;
    }
  }
  return true;
}