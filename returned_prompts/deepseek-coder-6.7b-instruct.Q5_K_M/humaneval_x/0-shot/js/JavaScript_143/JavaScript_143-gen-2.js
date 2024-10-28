  const isPrime = (num) => {
    for(let i = 2, sqrt = Math.sqrt(num); i <= sqrt; i++)
      if(num % i === 0) return false; 
    return num > 1;
  }

  return sentence.split(' ').filter(word => isPrime(word.length)).join(' ');
}

console.log(wordsInSentence("This is a test")); // "is"
console.log(wordsInSentence("lets go for swimming")); // "go for"

//  The function isPrime checks if a given number is a prime number or not.
//  The function wordsInSentence splits the given sentence into words and then filters out the words whose lengths are prime numbers.
//  The function returns a new string containing the filtered words.

//  In the test cases, the words "This" and "a" from the first sentence are not prime numbers (lengths: 4 and 1 respectively),
//  while the words "is" and "test" are prime numbers (lengths: 2 and 4 respectively), so they are the only words in the output sentences.
//  Similarly, the words "lets", "go", and "swimming" from the second sentence are not prime numbers (lengths: 4, 2 and 12 respectively),
//  while the words "for" is a prime number (length: 4), so it is the only word in the output sentence.
//  Hence, the output of the test cases matches the expected outputs.

//  This solution has a time complexity of O(n*m) where n is the number of words in the sentence and m is the average length of the words.
//  It also has a space complexity of O(n), where n is the number of words in the sentence.
//  The space complexity is due to the split function which creates an array of words.
//  The time complexity is due to the filter and join functions which iterate over the words in the sentence and create a new sentence.
//  The filter and join operations have a time complexity of O(n) where n is the number of words in the sentence.
//  The isPrime function has a time complexity of O(sqrt(m))