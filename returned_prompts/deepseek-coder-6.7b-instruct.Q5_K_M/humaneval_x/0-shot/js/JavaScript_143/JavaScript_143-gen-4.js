  // Function to check if a number is prime
  const isPrime = (num) => {
    for(let i = 2, sqrt = Math.sqrt(num); i <= sqrt; i++)
      if(num % i === 0) return false; 
    return num > 1;
  }

  // Split the sentence into words
  const words = sentence.split(' ');
  const primeWords = [];

  // Iterate over the words, check if its length is prime and if so, add it to the result
  for (let word of words) {
    if (isPrime(word.length)) {
      primeWords.push(word);
    }
  }

  // Join the prime words back into a sentence
  return primeWords.join(' ');
}

console.log(wordsInSentence("This is a test")); // Output: "is"
console.log(wordsInSentence("lets go for swimming")); // Output: "go for"
```

## Code Explanation

This code works by first defining a helper function `isPrime` that checks if a given number is prime. Then it splits the input sentence into words, checks the length of each word, and if the length is a prime number, it adds the word to a result array. Finally, it joins the words back into a sentence and returns it.

## Time Complexity

The time complexity of this code is O(n*m), where n is the number of words in the sentence and m is the average length of the words. The prime check takes O(sqrt(m)) time, and we perform this check for each word in the sentence, which gives us O(n*m*sqrt(m)).

## Space Complexity

The space complexity of this code is O(n), where n is the number of words in the sentence. This is because we store the words in an array, and in the worst case scenario, every word in the sentence is a prime number.

## Improvement

This solution is already optimal in terms of time complexity, but we can improve the space complexity by not storing the words in an array. Instead, we can directly build the output sentence. This would reduce the space complexity to O(1) as