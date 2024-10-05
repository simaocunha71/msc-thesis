  var result = [];
  for (const word of sentence.split(' ')) {
    if (isPrime(word.length)) {
      result.push(word);
    }
  }
  return result.join(' ');
}

function isPrime(n) {
  if (n < 2) {
    return false;
  }
  if (n == 2) {
    return true;
  }
  if (n % 2 == 0) {
    return false;
  }
  for (let i = 3; i * i <= n; i += 2) {
    if (n % i == 0) {
      return false;
    }
  }
  return true;
}



