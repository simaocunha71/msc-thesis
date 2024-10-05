  var words = sentence.split(' ');
  var prime_words = [];
  for (const word of words) {
    if (isPrime(word.length)) {
      prime_words.push(word);
    }
  }
  return prime_words.join(' ');
}



