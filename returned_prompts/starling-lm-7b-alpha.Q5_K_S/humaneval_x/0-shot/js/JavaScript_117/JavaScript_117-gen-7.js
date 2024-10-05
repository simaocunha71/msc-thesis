To solve this problem, you can follow these steps:

1. Create an array to store the words that have exactly n consonants.
2. Iterate through each word in the given string.
3. Check if the length of the word is greater than 0 (to avoid checking empty words).
4. If the length of the word is greater than 0, initialize a counter variable to keep track of the number of consonants in the word.
5. Iterate through each character in the word.
6. Check if the character is a consonant (you can use a function to determine if a character is a consonant).
7. If the character is a consonant, increment the counter variable.
8. After iterating through all the characters in the word, check if the counter variable is equal to n.
9. If the counter variable is equal to n, add the word to the array.
10. After iterating through all the words in the string, return the array.

Here's an example implementation in JavaScript:

function isConsonant(char) {
  return 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'.includes(char);
}

function selectWords(s, n) {
  const result = [];

  for (const word of s.split(' ')) {
    if (word.length > 0) {
      let count = 0;

      for (const char of word) {
        if (isConsonant(char)) {
          count++;
        }
      }

      if (count === n) {
        result.push(word);
      }
    }
  }

  return result;
}

You can use this function to solve the problem by passing the string and the desired number of consonants as arguments.

*/

function isConsonant(char) {
  return 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'.includes(char);
}

function selectWords(s, n) {
  const result = [];

  for (const word of s.split(' '