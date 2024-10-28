  // Helper function to calculate consonants in a word
  const countConsonants = (word) => {
    let count = 0;
    const consonants = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ';
    for (let i = 0; i < word.length; i++) {
      if (consonants.includes(word[i])) {
        count++;
      }
    }
    return count;
  };

  // If the string is empty, return an empty list
  if (s.length === 0) {
    return [];
  }

  // Split the string into words
  const words = s.split(' ');

  // Filter the words to only include those with n consonants
  const selectedWords = words.filter(word => countConsonants(word) === n);

  return selectedWords;
};

console.log(selectWords("Mary had a little lamb", 4)); // ["little"]
console.log(selectWords("Mary had a little lamb", 3)); // ["Mary"]
console.log(selectWords("simple white space", 2)); // []
console.log(selectWords("Hello world", 4)); // ["world"]
console.log(selectWords("Uncle sam", 3)); // ["Uncle"]

/*
This function works by first splitting the string s into a list of words using the split method.
Then it filters this list to only include the words that contain exactly n consonants.
To count the consonants in a word, it uses a helper function countConsonants which goes through each character in the word and checks if it is a consonant by checking if it is included in the string consonants.
If the character is a consonant, it increments the count.
Finally, it returns the list of words that contain exactly n consonants.
*/

/*
This function works by first splitting the string s into a list of words using the split method.
Then it filters this list to only include the words that contain exactly n consonants.
To count the consonants in a word, it uses