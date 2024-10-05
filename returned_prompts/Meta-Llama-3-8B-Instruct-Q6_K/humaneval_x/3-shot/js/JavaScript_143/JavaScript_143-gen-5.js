  let result = [];
  let words = sentence.split(" ");
  for (let word of words) {
    if (isPrime(word.length)) {
      result.push(word);
    }
  }
  return result.join(" ");
}

function isPrime(n) {
  if (n <= 1) return false;
  for (let i = 2, sqrt = Math.sqrt(n); i <= sqrt; i++) {
    if (n % i === 0) return false;
  }
  return true;
}