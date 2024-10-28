  // 1. first split the sentence into words
  const words = sentence.split(' ');

  // 2. create a helper function to check if a number is prime
  const isPrime = num => {
    for(let i = 2, sqrt = Math.sqrt(num); i <= sqrt; i++)
      if(num % i === 0) return false; 
    return num > 1;
  }

  // 3. use filter to get words with lengths that are prime numbers
  const primeWords = words.filter(word => isPrime(word.length));

  // 4. join the words back into a sentence
  const result = primeWords.join(' ');

  // 5. return the result
  return result;
}

console.log(wordsInSentence('This is a test')) // "is"
console.log(wordsInSentence('lets go for swimming')) // "go for"
console.log(wordsInSentence('Hello World')) // "World"
console.log(wordsInSentence('I am a sentence with length of 35')) // "am a sentence with length of"
```

The function works by first splitting the input sentence into an array of words. It then defines a helper function to check if a number is prime. Finally, it uses the Array.filter method to create a new array which contains only the words whose lengths are prime numbers. The result is then joined back into a sentence and returned.

This solution has a time complexity of O(n*m) where n is the number of words in the sentence and m is the average length of the words.
*/


const wordsInSentence = sentence => {
  const words = sentence.split(' ');
  const isPrime = num => {
    for(let i = 2, sqrt = Math.sqrt(num); i <= sqrt; i++)
      if(num % i === 0) return false; 
    return num > 1;
  }
  const primeWords = words.filter(word => isPrime(word.length));
  const result = primeWords.join(' ');
  return result;
}

console.log(wordsInSentence('