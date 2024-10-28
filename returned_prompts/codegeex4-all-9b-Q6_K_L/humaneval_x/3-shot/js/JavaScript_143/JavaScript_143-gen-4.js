  const isPrime = (number) => {
    if (number < 2) return false;
    for (let i = 2; i <= Math.sqrt(number); i++) {
      if (number % i === 0) return false;
    }
    return true;
  }

  const words = sentence.split(' ');
  const result = words.filter(word => isPrime(word.length));
  return result.join(' ');
}

