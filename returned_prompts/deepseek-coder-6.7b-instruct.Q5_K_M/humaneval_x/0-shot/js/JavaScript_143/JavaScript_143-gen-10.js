  const words = sentence.split(' ')
  const primeWords = []

  const isPrime = (num) => {
    for(let i = 2, sqrt = Math.sqrt(num); i <= sqrt; i++)
      if(num % i === 0) return false; 
    return num > 1;
  }

  for(let word of words){
    if(isPrime(word.length)){
      primeWords.push(word)
    }
  }

  return primeWords.join(' ')
}

console.log(wordsInSentence("This is a test")) // "is"
console.log(wordsInSentence("lets go for swimming")) // "go for"


In the function wordsInSentence we first split the sentence into words. Then we use a helper function isPrime to check if the length of a word is a prime number. If it is we push it to the primeWords array. Finally we join the primeWords array into a string and return it.
*/


const wordsInSentence = (sentence) => {
  const words = sentence.split(' ')
  const primeWords = []

  const isPrime = (num) => {
    for(let i = 2, sqrt = Math.sqrt(num); i <= sqrt; i++)
      if(num % i === 0) return false; 
    return num > 1;
  }

  for(let word of words){
    if(isPrime(word.length)){
      primeWords.push(word)
    }
  }

  return primeWords.join(' ')
}

console.log(wordsInSentence("This is a test")) // "is"
console.log(wordsInSentence("lets go for swimming")) // "go for"



/*
function wordsInSentence(sentence) {
  const words = sentence.split(' ')
  const primeWords = words.filter(word => isPrime(word.length))
  return primeWords.join(' ')
}

const isPrime = num => {
  for(let i = 2,