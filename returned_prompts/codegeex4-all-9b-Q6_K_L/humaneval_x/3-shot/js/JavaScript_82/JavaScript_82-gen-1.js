  let length = string.length;
  if (length < 2) {
    return false;
  }
  for (let i = 2; i < length; i++) {
    if (length % i == 0) {
      return false;
    }
  }
  return true;
}