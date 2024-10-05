  const words = sentence.split(' ');
  const primeLengths = [];

  for (const word of words) {
    const length = word.length;
    if (isPrime(length)) {
      primeLengths.push(length);
    }
  }

  const result = [];

  for (const length of primeLengths) {
    for (const word of words) {
      if (word.length == length) {
        result.push(word);
        break;
      }
    }
  }

  return result.join(' ');
}

const isPrime = (n) => {
  if (n <= 1) {
    return false;
  }
  for (let i = 2; i <= Math.sqrt(n); i++) {
    if (n % i === 0) {
      return false;
    }
  }
  return true;
}