  let arr = sentence.split(' ');
  let prime_words = [];

  for (const word of arr) {
    if (isPrime(word.length)) {
      prime_words.push(word);
    }
  }

  return prime_words.join(' ');
}



