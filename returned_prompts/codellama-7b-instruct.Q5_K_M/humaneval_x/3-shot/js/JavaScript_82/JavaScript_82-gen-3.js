  const length = string.length;
  for (let i = 2; i < length; i++) {
    if (length % i === 0) {
      return false;
    }
  }
  return true;
}



