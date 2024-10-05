const wordsInSentence = (sentence) => {

    let result = ""

    const sentenceArray = sentence.split(" ")
    for (let i = 0; i < sentenceArray.length; i++) {
      if (isPrime(sentenceArray[i].length)) {
        result += sentenceArray[i] + " "
      }
    }
    return result.trim()
  };

  function isPrime(n) {
    if (n < 2) return false
    for (let i = 2; i * i <= n; i++) {
      if (n % i === 0) return false
    }
    return true
  }

  console.log(wordsInSentence("This is a test"))
  console.log(wordsInSentence("lets go for swimming"))


  */

*/


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
