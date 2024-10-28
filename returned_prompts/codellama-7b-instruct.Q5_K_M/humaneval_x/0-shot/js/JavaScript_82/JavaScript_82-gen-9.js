const primeLength = (string) => {
  const len = string.length;
  for (let i = 2; i < len; i++) {
    if (len % i === 0) {
      return false;
    }
  }
  return true;
};

