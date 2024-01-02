/*Write a function that accepts a list of strings.
  The list contains different words. Return the word with maximum number
  of unique characters. If multiple strings have maximum number of unique
  characters, return the one which comes first in lexicographical order.

  findMax(["name", "of", "string"]) === "string"
  findMax(["name", "enam", "game"]) === "enam"
  findMax(["aaaaaaa", "bb" ,"cc"]) === ""aaaaaaa"
  */
const findMax = (words) => {
  let maxUniqueCharacters = 0;

  let sortedWords = words.sort((a,b)=> a.localeCompare(b));
  
  for(let i=0;i<sortedWords.length;i++){
    if (sortedWords[i].length > maxUniqueCharacters) {
      maxUniqueCharacters = sortedWords[i].length;
      // return the first index in the array that has a maximum length of unique characters 
      //return i;
    }
  }
  
  return (maxUniqueCharacters > 0 ? sortedWords[maxUniqueCharacters-1] : '');
}
