You can use the `split` and `join` methods to solve this problem. Here is a possible solution:

```javascript
const fixSpaces = (text) => {
  const words = text.split(" ");
  let result = "";
  
  for (let i = 0; i < words.length; i++) {
    if (words[i] === "") {
      if (result.slice(-1) === "-") {
        continue;
      }
      result += "-";
    } else {
      result += words[i];
    }
    if (i !== words.length - 1) {
      result += "_";
    }
  }
  
  return result;
}
```

This solution splits the input string into an array of words using the `split` method, and then iterates through the array. If the current word is an empty string (i.e., there are consecutive spaces), it checks if the last character of the result string is a dash. If it is, it continues to the next iteration. Otherwise, it adds a dash to the result string. If the current word is not an empty string, it adds the word to the result string, and if it is not the last word, it adds an underscore. Finally, it returns the result string.