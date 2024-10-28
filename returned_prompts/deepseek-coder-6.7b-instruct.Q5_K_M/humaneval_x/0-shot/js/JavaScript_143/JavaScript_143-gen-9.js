  const isPrime = (num) => {
    for(let i = 2, sqrt = Math.sqrt(num); i <= sqrt; i++)
      if(num % i === 0) return false; 
    return num > 1;
  }
  
  const words = sentence.split(' ');
  let result = '';
  
  for(let word of words){
    if(isPrime(word.length)) result += `${word} `;
  }
  
  return result.trim();
}

console.log(wordsInSentence("This is a test")); // "is"
console.log(wordsInSentence("lets go for swimming")); // "go for"
```

The isPrime helper function is used to check if a number is prime or not. It loops through from 2 to the square root of the input number and checks if the input number is divisible by any of these numbers. If it is, the function returns false (the number is not prime). If it is not divisible by any of these numbers, the function returns true (the number is prime).

The main function takes a sentence string as input. It splits the sentence into words using the split method and stores these words in an array. It then loops through each word in the array and checks if the length of the word is a prime number using the isPrime helper function. If it is, it adds the word to the result string with a space after it. The function finally returns the result string with any trailing spaces removed using the trim method.

The time complexity of the solution is O(n*m) where n is the number of words in the sentence and m is the length of the longest word in the sentence. This is because for each word, we are looping through up to the square root of the word's length to check if it's a prime number. The space complexity is O(n) as we are storing the words in an array.

Note: This solution assumes that the input sentence only contains letters and spaces. If the input sentence may contain punctuation or other special characters, the isPrime function and the main function would need to be updated to handle these cases.
*/

// JavaScript code
const wordsInSentence = sentence => {
  const isPrime =