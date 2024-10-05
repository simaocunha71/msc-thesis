  let maxUniqueChars = 0;
  let maxWord = '';

  for (let word of words) {
    const uniqueChars = new Set(word.split('')).size;
    if (uniqueChars > maxUniqueChars) {
      maxUniqueChars = uniqueChars;
      maxWord = word;
    } else if (uniqueChars === maxUniqueChars) {
      maxWord = word < maxWord ? word : maxWord;
    }
  }

  return maxWord;
};

console.log(findMax(["name", "of", "string"])) // === "string"
console.log(findMax(["name", "enam", "game"])) // === "enam"
console.log(findMax(["aaaaaaa", "bb" ,"cc"])) // === "aaaaaaa"

// Time Complexity: O(n*m) where n is the number of words in the list and m is the length of the longest word.
// Space Complexity: O(1) as we are using constant amount of space.

// This code assumes that the input will always be valid and does not handle any exceptions.

// The function works by iterating over each word in the input list. For each word, it splits the word into individual characters and adds them to a Set. This automatically removes any duplicate characters. The size of the Set is the number of unique characters in the word. If this number is greater than the current maximum number of unique characters found, the word is updated as the new maximum. If the number of unique characters is equal to the current maximum, the word is compared lexicographically and the lexicographically smaller one is kept. Finally, the word with the maximum number of unique characters is returned.

// Note: The space complexity is constant because we are not using any data structures that grow with the input size. We are only using a small number of variables that do not depend on the size of the input.

// This code assumes that the input will always be valid and does not handle any exceptions.

// The function works by iterating over each word in the input list. For each word, it splits the word into individual characters and adds them to a Set. This automatically removes any duplicate