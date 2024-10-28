  const length = string.length;
  if (length <= 1) {
    return false;
  }
  for (let i = 2; i <= Math.sqrt(length); i++) {
    if (length % i === 0) {
      return false;
    }
  }
  return true;
}