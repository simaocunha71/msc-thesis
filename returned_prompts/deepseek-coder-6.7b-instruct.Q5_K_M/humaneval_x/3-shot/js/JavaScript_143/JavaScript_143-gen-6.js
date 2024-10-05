  const isPrime = (n) => {
    if (n < 2) return false;
    for (let i = 2; i * i <= n; i++) {
      if (n % i === 0) return false;
    }
    return true;
  };

  const words = sentence.split(" ");
  const result = [];

  for (const word of words) {
    if (isPrime(word.length)) {
      result.push(word);
    }
  }

  return result.join(" ");
}



