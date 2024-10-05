  // Splitting the string into sentences
  let sentences = S.match(/[^.!\?]+[\.!\?]+/g);
  let boredoms = 0;
  
  // Checking each sentence to see if it starts with 'I'
  for (let sentence of sentences) {
    if (sentence.trim().charAt(0) === 'I') {
      boredoms++;
    }
  }
  
  return boredoms;
}
*/

const isBored = (S) => {
  let sentences = S.match(/[^.!\?]+[\.!\?]+/g);
  let boredoms = 0;
  
  for (let sentence of sentences) {
    if (sentence.trim().charAt(0) === 'I') {
      boredoms++;
    }
  }
  
  return boredoms;
}

module.exports = isBored;

/*
Test Cases:
console.log(isBored("Hello world")); // returns 0
console.log(isBored("The sky is blue. The sun is shining. I love this weather")); // returns 1
console.log(isBored("I am bored. What are you doing?")); // returns 1
console.log(isBored("I am bored. What are you doing. I am happy")); // returns 2
*/

// Solution: 
// This problem is asking to count the number of sentences that start with 'I' in a given string. 
// This can be done by splitting the string into sentences first, and then checking each sentence. 
// If the sentence starts with 'I', increment the count of boredoms.
// Finally, return the count of boredoms.











































































































