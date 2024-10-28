  let words = sentence.split(' ');
  let result = [];

  for (let word of words) {
    if (isPrime(word.length)) {
      result.push(word);
    }
  }

  return result.join(' ');
}



