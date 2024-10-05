You can solve this problem by using the built-in `split()` function to split the string into sentences, and then check if each sentence starts with the word "I". If it does, increment a counter variable. Finally, return the counter variable.
Here is the solution in JavaScript:
```javascript
const isBored = (S) => {
  const sentences = S.split(/[.?!]/);
  let count = 0;
  for (let sentence of sentences) {
    if (sentence.trim().startsWith("I")) {
      count++;
    }
  }
  return count;
}
```
You can test this function with the provided examples:
```javascript
console.log(isBored("Hello world")); // 0
console.log(isBored("The sky is blue. The sun is shining. I love this weather")); // 1
```