  const result = [];
  for (const word of sentence.split(' ')) {
    if (isPrime(word.length)) {
      result.push(word);
    }
  }
  return result.join(' ');
}



