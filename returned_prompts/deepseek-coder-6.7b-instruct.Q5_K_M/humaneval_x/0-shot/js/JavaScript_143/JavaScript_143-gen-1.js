  const words = sentence.split(' ');
  const primeWords = [];

  const isPrime = num => {
    if (num < 2) return false;
    for (let i = 2, sqrt = Math.sqrt(num); i <= sqrt; i++)
      if (num % i === 0) return false;
    return true;
  };

  for (let word of words) {
    if (isPrime(word.length)) primeWords.push(word);
  }

  return primeWords.join(' ');
};

console.log(wordsInSentence("This is a test"));  // "is"
console.log(wordsInSentence("lets go for swimming"));  // "go for"
```

### 5. 
```
