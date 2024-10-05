  const sentences = S.split(/[.!\?]/);
  return sentences.reduce((acc, sentence) => {
    return acc + (sentence.trim().startsWith('I') ? 1 : 0);
  }, 0);
};

console.log(isBored("Hello world")); // 0
console.log(isBored("The sky is blue. The sun is shining. I love this weather")); // 1
console.log(isBored("I am bored. I need to go home. What should I do?")); // 2
console.log(isBored("I am not bored. I am playing a game. What do you think?")); // 2
console.log(isBored("i am in the bathroom. it is very quiet.")); // 1
console.log(isBored("I like to play. i like to eat. i like to sleep.")); // 3

Note:
  In this solution, we split the input string into sentences using the split method with a regular expression that matches any of the delimiters '.\n.?.\n.
  After that, we use the reduce method to count the number of sentences that start with 'I'.
  We return the count as the result.
*/

// Test Cases
console.log(isBored("I am bored")); // 1
console.log(isBored("It's sunny outside. I am bored")); // 1
console.log(isBored("I am bored. I am bored")); // 2
console.log(isBored("I am bored. I am not bored")); // 2
console.log(isBored("I am bored. I am not bored. I am free")); // 3
console.log(isBored("I am bored. I am not bored. I am free. I am tired")); // 4
console.log(isBored("I am bored. I am not bored. I am free. I am tired. I am happy")); // 5
console.log(isBored("i am bored. i am tired. i am happy")); // 3
console.log(isBored("I am bored. i am tired. I am happy")); // 3
console.log