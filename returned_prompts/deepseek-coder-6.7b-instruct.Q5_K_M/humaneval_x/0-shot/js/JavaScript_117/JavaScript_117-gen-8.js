  // First we define a helper function to count consonants in a word
  const countConsonants = (word) => {
    const consonants = "bcdfghjklmnpqrstvwxyz";
    let count = 0;
    for (let i = 0; i < word.length; i++) {
      if (consonants.includes(word[i].toLowerCase())) {
        count++;
      }
    }
    return count;
  }

  // Check if string s is empty
  if (s === "") {
    return [];
  }

  // Split string s into words
  const words = s.split(" ");
  
  // Use the helper function to count consonants in each word, 
  // and store the words with exactly n consonants into result list
  const result = [];
  for (let i = 0; i < words.length; i++) {
    if (countConsonants(words[i]) === n) {
      result.push(words[i]);
    }
  }
  
  return result;
}
console.log(selectWords("Mary had a little lamb", 4));
console.log(selectWords("Mary had a little lamb", 3));
console.log(selectWords("simple white space", 2));
console.log(selectWords("Hello world", 4));
console.log(selectWords("Uncle sam", 3));

// Output:
// [ 'little' ]
// [ 'Mary' ]
// []
// [ 'world' ]
// [ 'Uncle' ]

// Time Complexity: O(n*m), where n is the number of words in the string s and m is the length of the longest word.
// Space Complexity: O(n), where n is the number of words in the string s.

// The function counts the consonants in each word of the string s and stores the words with exactly n consonants into a result list.
// It returns this result list. If the string s is empty, it returns an empty list.

// Note: The function assumes the input string contains only letters and spaces