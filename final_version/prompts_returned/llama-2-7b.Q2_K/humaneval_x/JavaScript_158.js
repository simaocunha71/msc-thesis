/*Write a function that accepts a list of strings.
  The list contains different words. Return the word with maximum number
  of unique characters. If multiple strings have maximum number of unique
  characters, return the one which comes first in lexicographical order.

  findMax(["name", "of", "string"]) === "string"
  findMax(["name", "enam", "game"]) === "enam"
  findMax(["aaaaaaa", "bb" ,"cc"]) === ""aaaaaaa"
  */
const findMax = (words) => {
  let max;
  words.forEach((w)=>{if(count(w)) count(w, {})>max?({}={}):{}});
  return max;
};
