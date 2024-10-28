  let maxUnique = 0;
  let maxWord = '';

  for (let word of words) {
    const uniqueChars = new Set(word.split('')).size;
    if (uniqueChars > maxUnique) {
      maxUnique = uniqueChars;
      maxWord = word;
    } else if (uniqueChars === maxUnique) {
      maxWord = maxWord < word ? maxWord : word;
    }
  }

  return maxWord;
};

console.log(findMax(["name", "of", "string"])); // "string"
console.log(findMax(["name", "enam", "game"])); // "enam"
console.log(findMax(["aaaaaaa", "bb" ,"cc"])); // "aaaaaaa"

*/

const findMax = (words) => {
  let maxUnique = 0;
  let maxWord = '';

  for (let word of words) {
    const uniqueChars = new Set(word.split('')).size;
    if (uniqueChars > maxUnique) {
      maxUnique = uniqueChars;
      maxWord = word;
    } else if (uniqueChars === maxUnique) {
      maxWord = maxWord < word ? maxWord : word;
    }
  }

  return maxWord;
};

console.log(findMax(["name", "of", "string"])); // "string"
console.log(findMax(["name", "enam", "game"])); // "enam"
console.log(findMax(["aaaaaaa", "bb", "cc"])); // "aaaaaaa"
