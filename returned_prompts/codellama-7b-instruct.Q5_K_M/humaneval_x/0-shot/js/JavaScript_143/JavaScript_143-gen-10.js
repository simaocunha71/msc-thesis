  const sentenceWords = sentence.split(" ");
  const primeNumbers = [];
  const newSentence = [];

  for (let i = 0; i < sentenceWords.length; i++) {
    if (isPrime(sentenceWords[i].length)) {
      primeNumbers.push(sentenceWords[i]);
    }
  }

  for (let j = 0; j < primeNumbers.length; j++) {
    newSentence.push(primeNumbers[j]);
  }

  return newSentence.join(" ");
};

const isPrime = (number) => {
  if (number === 2) return true;
  if (number % 2 === 0 || number % 3 === 0) return false;
  for (let i = 5; i * i <= number; i = i + 6) {
    if (number % i === 0 || number % (i + 2) === 0) return false;
  }
  return true;
};

console.log(wordsInSentence("This is a test")); // "is"
console.log(wordsInSentence("lets go for swimming")); // "go for"
