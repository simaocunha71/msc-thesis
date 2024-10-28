  const isPrime = (num) => {
    for (let i = 2; i <= Math.sqrt(num); i++) {
      if (num % i === 0) return false;
    }
    return num > 1;
  };

  const words = sentence.split(' ');
  const primeWords = words.filter(word => isPrime(word.length));
  return primeWords.join(' ');
}