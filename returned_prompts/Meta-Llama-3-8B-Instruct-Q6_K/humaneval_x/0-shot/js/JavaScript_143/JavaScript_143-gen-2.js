```
const wordsInSentence = (sentence) => {
  const words = sentence.split(' ');
  const result = [];
  for (const word of words) {
    if (isPrime(word.length)) {
      result.push(word);
    }
  }
  return result.join(' ');
};

const isPrime = (num) => {
  if (num <= 1) return false;
  for (let i = 2, sqrt = Math.sqrt(num); i <= sqrt; i++) {
    if (num % i === 0) return false;
  }
  return true;
};
```
The code first splits the input sentence into words using the `split` method. Then, it iterates over the words and checks if the length of each word is a prime number using the `isPrime` function. If it is, the word is added to the result array. Finally, the code joins the result array into a string using the `join` method and returns it. The `isPrime` function checks if a number is prime by iterating from 2 to the square root of the number and checking if the number is divisible by any of these values. If it is, the function returns `false`, otherwise it returns `true`.