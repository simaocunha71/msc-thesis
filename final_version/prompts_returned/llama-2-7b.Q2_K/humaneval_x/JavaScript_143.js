/*
  You are given a string representing a sentence,
  the sentence contains some words separated by a space,
  and you have to return a string that contains the words from the original sentence,
  whose lengths are prime numbers,
  the order of the words in the new string should be the same as the original one.

  Example 1:
      Input: sentence = "This is a test"
      Output: "is"

  Example 2:
      Input: sentence = "lets go for swimming"
      Output: "go for"

  Constraints:
      * 1 <= len(sentence) <= 100
      * sentence contains only letters
  */
const wordsInSentence = (sentence) => {
    let outputString = "";
    const sentenceArray = sentence.split(' ');
    for (let i = sentenceArray.length - 1; i > -1 && i >= 0 ; --i){
        if(sentenceArray[i] == "") continue;
        if((sentenceArray[i]) % 2 !== 0) outputString += " " + sentenceArray[i];
    }
    return outputString;
};
module.exports = wordsInSentence