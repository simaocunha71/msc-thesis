  let words = sentence.split(' ');
  let result = '';
  for (let word of words) {
    let length = word.length;
    if (isPrime(length)) {
      result += word + ' ';
    }
  }
  return result.trim();
}

function isPrime(n) {
  if (n <= 1) {
    return false;
  }
  for (let i = 2; i * i <= n; i++) {
    if (n % i === 0) {
      return false;
    }
  }
  return true;
}