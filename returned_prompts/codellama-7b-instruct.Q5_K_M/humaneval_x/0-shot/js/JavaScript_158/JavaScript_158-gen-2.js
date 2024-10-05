/*Write a function that accepts a list of strings.
  The list contains different words. Return the word with maximum number
  of unique characters. If multiple strings have maximum number of unique
  characters, return the one which comes first in lexicographical order.

  findMax(["name", "of", "string"]) === "string"
  findMax(["name", "enam", "game"]) === "enam"
  findMax(["aaaaaaa", "bb" ,"cc"]) === ""aaaaaaa"
  */
const findMax = (words) => {
  let max = 0
  let word = ""
  for (let i = 0; i < words.length; i++) {
    if (words[i].length > max) {
      max = words[i].length
      word = words[i]
    }
  }
  return word
}
