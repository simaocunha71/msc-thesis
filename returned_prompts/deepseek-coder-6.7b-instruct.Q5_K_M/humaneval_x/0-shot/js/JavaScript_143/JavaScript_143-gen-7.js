  const isPrime = (n) => {
    if (n < 2) {
      return false;
    }
    for (let i = 2; i <= Math.sqrt(n); i++) {
      if (n % i === 0) {
        return false;
      }
    }
    return true;
  }

  const words = sentence.split(' ');
  let result = '';

  for (let i = 0; i < words.length; i++) {
    if (isPrime(words[i].length)) {
      result += words[i] + ' ';
    }
  }

  return result.trim();
}

console.log(wordsInSentence("This is a test")); // Output: "is"
console.log(wordsInSentence("lets go for swimming")); // Output: "go for"
```

Here, we define a helper function `isPrime` to check if a number is prime or not. Then, we split the input sentence into an array of words and loop through each word. If the length of a word is a prime number, we add it to the result string. Finally, we return the result string after removing any trailing spaces.

The time complexity of this solution is O(n*sqrt(m)), where n is the number of words in the sentence and m is the length of the longest word in the sentence. This is because for each word in the sentence, we perform a loop up to the square root of the word's length, which is the worst-case scenario for checking if a number is prime. The space complexity is O(n), where n is the number of words in the sentence, as we store the words in an array.

Note: The helper function `isPrime` checks if a number is prime by iterating from 2 to the square root of the number and checking if the number is divisible by any of these numbers. If it is, the number is not prime, and the function returns false. If the number is not divisible by any of these numbers, it is prime, and the function returns true.
*/
```

## Python Code
```python
def is_prime(n):
    if n < 2:
        return False
    for i in range(