/*
  * 1) split the sentence into an array of words
  * 2) loop through the array of words and check if the word's length is prime
  * 3) if it's prime, push it into a new array
  * 4) join the new array and return it
*/
const wordsInSentence = (sentence) => {
  const words = sentence.split(' ');
  const newWords = [];
  for (const word of words) {
    if (isPrime(word.length)) {
      newWords.push(word);
    }
  }
  return newWords.join(' ');
};

const isPrime = (n) => {
  if (n <= 1) {
    return false;
  }
  for (let i = 2; i < n; i++) {
    if (n % i === 0) {
      return false;
    }
  }
  return true;
};
