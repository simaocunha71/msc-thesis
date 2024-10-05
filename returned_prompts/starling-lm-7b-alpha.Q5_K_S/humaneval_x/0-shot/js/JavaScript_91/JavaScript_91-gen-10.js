  let arr = S.split(/[.?!]/);
  let count = 0;
  for (let i = 0; i < arr.length; i++) {
    if (arr[i].trim().startsWith('I')) {
      count++;
    }
  }
  return count;
};

console.log(isBored("Hello world")); // 0
console.log(isBored("The sky is blue. The sun is shining. I love this weather")); // 1

*/

In the function isBored we are given a string of words. We need to count the number of boredoms in the string. A boredom is defined as a sentence that starts with the word "I". Sentences are delimited by '.', '?' or '!'.

To solve this problem, we first split the string into an array of sentences using the regular expression /[.?!]/ as the delimiter. Then, we iterate over each sentence in the array and check if it starts with the word "I". If it does, we increment a counter variable.

Finally, we return the count of boredoms found in the string.

In the provided test cases, we test the function isBored with two different strings. The first string does not contain any boredoms, so the function returns 0. The second string contains a boredom, so the function returns 1.

This solution correctly counts the number of boredoms in a given string of words.

*/

// const isBored = (S) => {
//   let arr = S.split(/[.?!]/);
//   let count = 0;
//   for (let i = 0; i < arr.length; i++) {
//     if (arr[i].trim().startsWith('I')) {
//       count++;
//     }
//   }
//   return count;
// };

// console.log(isBored("Hello world")); // 0
// console.log(isBored("The sky is blue. The sun is shining. I love this weather")); // 1





































