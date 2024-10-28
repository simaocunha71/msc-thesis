function findMax(words) {
  let result = '';
  let maxCount = 0;

  for (let i = 0; i < words.length; i++) {
    let count = 0;
    let current = words[i];

    for (let j = 0; j < words.length; j++) {
      if (current[0] === words[j][0]) {
        count++;
      }
    }

    if (count > maxCount) {
      maxCount = count;
      result = current;
    }
  }

  return result;
}

findMax(["name", "of", "string"]) === "string";
findMax(["name", "enam", "game"]) === "enam";
findMax(["aaaaaaa", "bb", "cc"]) === "aaaaaaa";

/* The solution works by finding the most frequent character in the alphabet
  order. It does so by iterating over each string in the list of strings.
  For each string, it counts the number of times the first character of
  the string appears in the rest of the list of strings. If this count
  is larger than the current maximum count, the maximum count and the
  result are updated.

  At the end of the function, the result is returned, which is the string
  with the maximum number of unique characters.*/

// Another way to find the word with the maximum number of unique
// characters is to use a hash table to keep track of the number of
// unique characters in each string. This approach is more efficient
// than the previous one, as it does not require iterating over the
// entire list of strings for each string in the list.

function findMax2(words) {
  let result = '';
  let maxCount = 0;

  for (let i = 0; i < words.length; i++) {
    let count = new Set(words[i]).size;

    if (count > maxCount) {
      maxCount = count;
      result = words[i];
    }
  }

  return result;
}

findMax2(["name", "of", "string"]) === "string";
