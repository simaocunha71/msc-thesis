  let words = sentence.split(' ');
  let result = '';

  for (let i = 0; i < words.length; i++) {
    if (isPrime(words[i].length)) {
      result += words[i] + ' ';
    }
  }

  return result.trim();
}

// O(n^2)
function isPrime(n) {
  for (let i = 2; i <= Math.sqrt(n); i++) {
    if (n % i === 0) {
      return false;
    }
  }
  return n !== 1 && n !== 0;
}

// O(n)
function isPrime(n) {
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