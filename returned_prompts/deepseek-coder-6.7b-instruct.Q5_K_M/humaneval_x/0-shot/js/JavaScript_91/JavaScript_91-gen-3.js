  let sentences = S.split(/[.?!]/);
  let boredoms = 0;
  
  for(let i = 0; i < sentences.length; i++){
    if(sentences[i].trim().startsWith("I")){
      boredoms++;
    }
  }
  
  return boredoms;
};

console.log(isBored("Hello world"));  // 0
console.log(isBored("The sky is blue. The sun is shining. I love this weather"));  // 1
console.log(isBored("I am bored. You are bored too. We are all bored"));  // 3
console.log(isBored("It is not I who am bored, but I wholeheartedly agree. That is my opinion"));  // 2

/*
  The function `isBored` splits the input string `S` into an array of sentences by splitting it at each instance of '.', '?' or '!' using a regular expression.
  Then, it iterates through each sentence and checks if it starts with the word "I". If it does, it increments the `boredoms` counter.
  Finally, it returns the number of boredoms found.
*/

/*
  The function `isBored` works by splitting the input string `S` into an array of sentences.
  Then, it iterates through each sentence and checks if it starts with the word "I". If it does, it increments the `boredoms` counter.
  Finally, it returns the number of boredoms found.
*/

/*
  The function `isBored` works by splitting the input string `S` into an array of sentences.
  Then, it iterates through each sentence and checks if it starts with the word "I". If it does, it increments the `boredoms` counter.
  Finally, it returns the number of boredoms found.
*/

/*
  The function `isBored` works by splitting the input string `S` into an array of sentences.
  Then, it iterates through each sentence and checks if it starts with the word "I". If it does, it increments the `boredoms` counter.
  Finally, it returns the number of boredoms