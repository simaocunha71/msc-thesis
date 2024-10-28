/*
  1. split sentence by space
  2. filter words by length
  3. join words with space
  4. return
*/

const wordsInSentence = (sentence) => {
  const splitSentence = sentence.split(" ");
  const primeLengthWords = splitSentence.filter((word) => isPrime(word.length));
  return primeLengthWords.join(" ");
};

const isPrime = (num) => {
  if (num < 2) return false;
  for (let i = 2; i <= Math.sqrt(num); i++) {
    if (num % i === 0) return false;
  }
  return true;
};

console.log(wordsInSentence("This is a test"));
// Output: "is"

console.log(wordsInSentence("lets go for swimming"));
// Output: "go for"
*/