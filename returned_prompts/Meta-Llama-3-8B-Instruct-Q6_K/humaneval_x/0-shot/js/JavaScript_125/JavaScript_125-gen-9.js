```
const splitWords = (txt) => {
  if (txt.includes(' ')) {
    return txt.split(' ');
  } else if (txt.includes(',')) {
    return txt.split(',');
  } else {
    let count = 0;
    for (let i = 0; i < txt.length; i++) {
      if (txt[i].toLowerCase() >= 'a' && txt[i].toLowerCase() <= 'z' && (i + ord('a')) % 2 !== 0) {
        count++;
      }
    }
    return count;
  }
};
```


In this code, we first check if the input string contains any whitespace characters using the includes method. If it does, we split the string into an array of words using the split method with a space character as the separator.

If the string does not contain any whitespace characters, we then check if it contains any comma characters using the includes method again. If it does, we split the string into an array of words using the split method with a comma character as the separator.

If the string does not contain any whitespace or comma characters, we then iterate over each character in the string using a for loop. We check if each character is a lowercase letter between 'a' and 'z' (inclusive) using the toLowerCase method and the >= and <= operators. We also check if the position of the character in the alphabet is odd using the modulus operator (%). If both conditions are true, we increment a counter variable.

Finally, we return the value of the counter variable as the result. The function is designed to handle different types of input strings and return the correct result accordingly.