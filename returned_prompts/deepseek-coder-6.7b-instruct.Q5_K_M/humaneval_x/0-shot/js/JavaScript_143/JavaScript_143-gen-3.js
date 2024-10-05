  const isPrime = (num) => {
    for (let i = 2, sqrt = Math.sqrt(num); i <= sqrt; i++)
      if (num % i === 0) return false;
    return num > 1;
  }

  return sentence.split(' ').filter(word => isPrime(word.length)).join(' ');
}

console.log(wordsInSentence("This is a test")); // "is"
console.log(wordsInSentence("lets go for swimming")); // "go for"
```

This code works by splitting the sentence into an array of words, then filtering out those words that are not prime numbers in length. It uses the `isPrime` helper function to check the length of each word. Finally, it joins the remaining words back together into a string.

Please note that the length of the sentence must be less than or equal to 100 and the sentence must contain only letters.
*/

const wordsInSentence = (sentence) => {
  const isPrime = (num) => {
    for (let i = 2, sqrt = Math.sqrt(num); i <= sqrt; i++)
      if (num % i === 0) return false;
    return num > 1;
  }

  return sentence.split(' ').filter(word => isPrime(word.length)).join(' ');
}

console.log(wordsInSentence("This is a test")); // "is"
console.log(wordsInSentence("lets go for swimming")); // "go for"

module.exports = wordsInSentence;
```

## Question 2

```javascript
/*
