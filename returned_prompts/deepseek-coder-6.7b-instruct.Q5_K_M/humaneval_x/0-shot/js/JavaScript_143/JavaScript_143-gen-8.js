  // Split the sentence into words
  let words = sentence.split(" ");

  // Function to check if a number is prime
  const isPrime = (num) => {
    for(let i = 2; i < num; i++)
      if(num % i === 0) return false;
    return num > 1;
  }

  // Filter the words by their lengths
  words = words.filter(word => isPrime(word.length));

  // Join the filtered words back into a sentence
  return words.join(" ");
}

console.log(wordsInSentence("This is a test")); // "is"
console.log(wordsInSentence("lets go for swimming")); // "go for"

/*
  This solution works by first splitting the input sentence into words.
  Then it filters out the words that are not prime length.
  Finally, it joins the remaining words back into a sentence.
  */

/*
  The time complexity of this solution is O(n*m) where n is the number of words in the sentence
  and m is the average length of the words.
  The space complexity is O(n) as we are storing the words in an array.
  */

// This function works correctly as per the given problem statement.
// However, it has a bug in the isPrime function.
// The isPrime function is not efficient for large inputs.
// We can use the fact that all non-prime numbers are divisible by a prime number
// to optimize the isPrime function.

// This is the corrected function:

const isPrime = n => {
  if (n < 2) return false;
  for (let i = 2, sqrt = Math.sqrt(n); i <= sqrt; i++)
    if (n % i === 0) return false;
  return true;
}

const wordsInSentence = sentence => {
  return sentence.split(" ").filter(isPrime).join(" ");
}
```















































