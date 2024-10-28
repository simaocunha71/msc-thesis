  const isPrime = (num) => {
    for (let i = 2; i <= Math.sqrt(num); i++) {
      if (num % i === 0) {
        return false;
      }
    }
    return num > 1;
  };

  const words = sentence.split(" ");
  const result = words.filter(word => isPrime(word.length)).join(" ");

  return result;
}