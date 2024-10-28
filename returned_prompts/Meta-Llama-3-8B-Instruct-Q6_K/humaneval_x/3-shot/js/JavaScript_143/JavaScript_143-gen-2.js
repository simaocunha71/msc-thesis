  let words = sentence.split(' ');
  let result = '';

  for (let word of words) {
    if (isPrime(word.length)) {
      result += word + ' ';
    }
  }

  return result.trim();
}

function isPrime(n) {
  if (n <= 1) return false;
  if (n === 2) return true;
  if (n % 2 === 0) return false;

  let sqrt = Math.sqrt(n);

  for (let i = 3; i <= sqrt; i += 2) {
    if (n % i === 0) return false;
  }

  return true;
}