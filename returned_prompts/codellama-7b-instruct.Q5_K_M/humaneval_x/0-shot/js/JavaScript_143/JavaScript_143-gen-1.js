const wordsInSentence = (sentence) => {
  const words = sentence.split(' ');
  const primes = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97];
  const primeWords = [];
  words.forEach(word => {
    if (primes.includes(word.length)) {
      primeWords.push(word);
    }
  });
  return primeWords.join(' ');
};
