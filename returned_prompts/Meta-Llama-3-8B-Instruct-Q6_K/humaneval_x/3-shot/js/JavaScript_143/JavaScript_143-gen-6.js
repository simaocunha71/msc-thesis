  const words = sentence.split(' ');
  return words.filter(word => isPrime(word.length)).join(' ');
}

function isPrime(n) {
  if (n <= 1) return false;
  for (let i = 2, sqrt = Math.sqrt(n); i <= sqrt; i++)
    if (n % i === 0) return false;
  return true;
}