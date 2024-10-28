  let maxUniqueChars = 0;
  let maxWord = "";

  for (let word of words) {
    let uniqueChars = new Set(word.split("")).size;
    if (uniqueChars > maxUniqueChars) {
      maxUniqueChars = uniqueChars;
      maxWord = word;
    } else if (uniqueChars === maxUniqueChars) {
      maxWord = maxWord < word ? maxWord : word;
    }
  }

  return maxWord;
};

console.log(findMax(["name", "of", "string"]));
console.log(findMax(["name", "enam", "game"]));
console.log(findMax(["aaaaaaa", "bb", "cc"]));

*/

/*
const findMax = (words) => {
  let maxUniqueChars = 0;
  let maxWord = "";

  for (let word of words) {
    let uniqueChars = new Set(word.split("")).size;
    if (uniqueChars > maxUniqueChars) {
      maxUniqueChars = uniqueChars;
      maxWord = word;
    } else if (uniqueChars === maxUniqueChars) {
      maxWord = maxWord < word ? maxWord : word;
    }
  }

  return maxWord;
};

console.log(findMax(["name", "of", "string"]));
console.log(findMax(["name", "enam", "game"]));
console.log(findMax(["aaaaaaa", "bb", "cc"]));
*/

const findMax = (words) => {
  let maxUniqueChars = 0;
  let maxWord = "";

  for (let word of words) {
    let uniqueChars = new Set(word.split("")).size;
    if (uniqueChars > maxUniqueChars) {
      maxUniqueChars = uniqueChars;
      maxWord = word;
    } else if (uniqueChars === maxUniqueChars) {
      maxWord = maxWord < word ? maxWord : word