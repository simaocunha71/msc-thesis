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
    let wordArr = sentence.split(' ');
    if (!isPrime(wordArr[0])) return ''
    const resultWord = []
    for(let i=1;i<wordArr.length;i++){
        if(!isPrime(wordArr[i])) break;
        wordArr[i] = numberToString(wordArr[i]) 
        resultWord.push(wordArr[i]);
    }
    return resultWord.join(' ');
}
const isPrime = (number) => {
     let str = ''
      for(let i=2;i<number+1;i++){
          if((number % i === 0)) break;
          str += i + " ";
      }
    return str.length == 0 ? true : false;
}
const numberToString = (num) => { // returns 3456 as "three four five six"
    let arr=[];
    for(let i=1;i<=num+1;i++){arr.push(String(i))}
    return `${arr[0]}\t${arr[1]}\t\t...\t${arr[arr.length-1]}  `
}