  if (s === '') return [];
  
  const words = s.split(' ');
  const consonants = 'bcdfghjklmnpqrstvwxyz';
  let result = [];
  
  for (let word of words) {
    let count = 0;
    for (let char of word) {
      if (consonants.includes(char.toLowerCase())) count++;
    }
    if (count === n) result.push(word);
  }
  
  return result;
}

console.log(selectWords("Mary had a little lamb", 4)); // ["little"]
console.log(selectWords("Mary had a little lamb", 3)); // ["Mary"]
console.log(selectWords("simple white space", 2)); // []
console.log(selectWords("Hello world", 4)); // ["world"]
console.log(selectWords("Uncle sam", 3)); // ["Uncle"]

// In the solution, first we check if the string is empty and return an empty array if it is.
// Then we split the string into words and iterate over them.
// For each word, we count the number of consonants by checking each character if it is included in the consonants string.
// If the count equals to n, we push the word to the result array.
// Finally, we return the result array.
// Note that we convert each character to lower case to handle cases where the string contains uppercase letters.
// This solution assumes that words are separated by spaces and the string contains only letters and spaces.
// If the string contains punctuation, we need to adjust the solution accordingly.

/*
Time complexity: O(n*m), where n is the number of words in the string and m is the length of the longest word.
Space complexity: O(n), where n is the number of words in the string.
*/
/*
  In this solution, we iterate over each word in the string. For each word, we iterate over each character.
  If the character is a consonant, we increment a count. If the count equals n, we add the word to the result list.
  We return the result list at the end of