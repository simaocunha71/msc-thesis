  const words = sentence.split(' ');
  let result = '';
  for (const word of words) {
    if (isPrime(word.length)) {
      result += word + ' ';
    }
  }
  return result.trim();
}

function isPrime(n) {
  if (n <= 1) return false;
  for (let i = 2, sqrt = Math.floor(Math.sqrt(n)); i <= sqrt; i++) {
    if (n % i === 0) return false;
  }
  return true;
}