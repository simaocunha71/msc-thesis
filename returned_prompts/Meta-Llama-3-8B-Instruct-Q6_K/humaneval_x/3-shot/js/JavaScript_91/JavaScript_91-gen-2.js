  let boredomCount = 0;
  let sentence = '';
  for (let i = 0; i < S.length; i++) {
    if (S[i] == '.' || S[i] == '?' || S[i] == '!') {
      if (sentence.trim().startsWith('I')) {
        boredomCount++;
      }
      sentence = '';
    } else {
      sentence += S[i];
    }
  }
  if (sentence.trim().startsWith('I')) {
    boredomCount++;
  }
  return boredomCount;
}  // 1
// console.log(isBored("Hello world")); // 0
// console.log(isBored("The sky is blue. The sun is shining. I love this weather")); // 1
// console.log(isBored("I am happy")); // 1
// console.log(isBored("I am very happy. I am very very happy.")); // 2
// console.log(isBored("I love to code. I love coding.")); // 2
// console.log(isBored("I love to code. I love coding. I love coding.")); // 3
// console.log(isBored("Hello world! I am a coder. I am a happy coder.")); // 2
// console.log(isBored("Hello world! I am a coder. I am a happy coder. I am a very happy coder.")); // 3
// console.log(isBored("Hello world")); // 0
// console.log(isBored("The sky is blue. The sun is shining.")); // 0
// console.log(isBored("I love this weather")); // 1
// console.log(isBored("I love this weather. I love this weather.")); // 2
// console.log(isBored("I love this weather. I love this weather. I love this weather.")); // 3
// console.log(isBored("Hello world! The sky is blue. The sun is shining. I love this weather")); // 1
// console.log(isBored("Hello world! The sky is blue. The sun is shining. I love this weather. I love this weather.")); // 2
// console.log(isBored("Hello world! The sky is blue. The sun is shining. I love this weather. I love this weather. I love this weather.")); // 3
// console.log(isBored("Hello world