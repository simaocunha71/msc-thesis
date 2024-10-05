/*
  You are given a string representing a sentence,
  the sentence contains some words separated by a space,
  and you have to return a string that contains the words from the original sentence,
  whose lengths are prime numbers,
  the order of the words in the new string should be the same as the original one.

  Example 1:
      Input: sentence = "This is a test"
      Output: "is"

  Example 2:
      Input: sentence = "lets go for swimming"
      Output: "go for"

  Constraints:
      * 1 <= len(sentence) <= 100
      * sentence contains only letters
  */
const wordsInSentence = (sentence) => {
  const words = sentence.split(' ');
  const primeWords = [];

  for (const word of words) {
    if (isPrime(word.length)) {
      primeWords.push(word);
    }
  }

  return primeWords.join(' ');
};

const isPrime = (num) => {
  if (num < 2) return false;

  for (let i = 2; i <= Math.sqrt(num); i++) {
    if (num % i === 0) return false;
  }

  return true;
};

console.log(wordsInSentence("This is a test")); // "is"
console.log(wordsInSentence("lets go for swimming")); // "go for"