  // Initialize empty list to store words with n consonants
  let wordsWithNConsonants = [];

  // Define consonants
  const consonants = "bcdfghjklmnpqrstvwxyz";

  // Split the string s into words
  let words = s.split(" ");

  // Loop over each word in the words list
  for (let word of words) {

    // Initialize count of consonants in the current word
    let consonantCount = 0;

    // Loop over each character in the current word
    for (let char of word) {

      // If the character is a consonant, increment the consonant count
      if (consonants.includes(char.toLowerCase())) {
        consonantCount++;
      }
    }

    // If the word has exactly n consonants, add it to the wordsWithNConsonants list
    if (consonantCount === n) {
      wordsWithNConsonants.push(word);
    }
  }

  // Return the wordsWithNConsonants list
  return wordsWithNConsonants;
};
console.log(selectWords("Mary had a little lamb", 4));  // ["little"]
console.log(selectWords("Mary had a little lamb", 3));  // ["Mary"]
console.log(selectWords("simple white space", 2));  // []
console.log(selectWords("Hello world", 4));  // ["world"]
console.log(selectWords("Uncle sam", 3));  // ["Uncle"]




























































































































