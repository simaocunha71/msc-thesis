  var words = sentence.split(' ');
  var prime_words = [];

  for (const word of words) {
    if (isPrime(word.length)) {
      prime_words.push(word);
    }
  }

  return prime_words.join(' ');
}

const isPrime = (num) => {
  if (num <= 1) {
    return false;
  }
  for (let i = 2; i < num; i++) {
    if (num % i == 0) {
      return false;
    }
  }
  return true;
}