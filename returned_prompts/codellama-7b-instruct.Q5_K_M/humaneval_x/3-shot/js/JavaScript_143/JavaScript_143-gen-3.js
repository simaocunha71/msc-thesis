  var result = [];
  var words = sentence.split(' ');

  for (let word of words) {
    if (isPrime(word.length)) {
      result.push(word);
    }
  }

  return result.join(' ');
}



