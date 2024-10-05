function primeLength(string) {
  if (string.length === 1) return false;

  for (let i = 2; i < string.length; i++) {
    if (string.length % i === 0) return false;
  }
  return true;
}

const primeLength = (string) => {
  let isPrime = true;
  for (let i = 2; i < string.length; i++) {
    if (string.length % i === 0) {
      isPrime = false;
      break;
    }
  }
  return isPrime;
};

const primeLength = (string) => {
  for (let i = 2; i < string.length; i++) {
    if (string.length % i === 0) return false;
  }
  return true;
};
