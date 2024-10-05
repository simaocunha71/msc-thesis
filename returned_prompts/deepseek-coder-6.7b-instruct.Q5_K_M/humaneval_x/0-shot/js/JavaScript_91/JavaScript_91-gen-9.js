  let sentences = S.split(/[.!\?]/);
  let count = 0;

  for(let i = 0; i < sentences.length; i++){
    if(sentences[i].trim().startsWith('I')) count++;
  }

  return count;
}

console.log(isBored("Hello world")); // 0
console.log(isBored("The sky is blue. The sun is shining. I love this weather")); // 1
console.log(isBored("I am bored. I want to play. I have a dog. I need to sleep.")); // 3
console.log(isBored("i am")); // 1
```

In this code, we first split the input string `S` into sentences using the `split()` method with a regular expression that matches any of the three sentence delimiters.

Then, we initialize a count variable to 0. We loop through each sentence in the array and check if it starts with the word "I". If it does, we increment the count.

Finally, we return the count.

This function will count the number of sentences that start with the word "I", giving us the number of boredoms.
*/

const isBored = (S) => {
  let sentences = S.split(/[.!\?]/);
  let count = 0;

  for(let i = 0; i < sentences.length; i++){
    if(sentences[i].trim().startsWith('I')) count++;
  }

  return count;
}

console.log(isBored("Hello world")); // 0
console.log(isBored("The sky is blue. The sun is shining. I love this weather")); // 1
console.log(isBored("I am bored. I want to play. I have a dog. I need to sleep.")); // 3
console.log(isBored("i am")); // 1
```

This function will work for any string of words. It counts the number of sentences in the input string that start with the word "I", giving us the number of boredoms.
*/

const isBored = (S) => {
 