  const words = sentence.split(' ');
  const isPrime = (num) => {
    if (num < 2) return false;
    for (let i = 2; i <= Math.sqrt(num); i++) {
      if (num % i === 0) return false;
    }
    return true;
  };
  const primeWords = words.filter(word => isPrime(word.length));
  return primeWords.join(' ');
}



