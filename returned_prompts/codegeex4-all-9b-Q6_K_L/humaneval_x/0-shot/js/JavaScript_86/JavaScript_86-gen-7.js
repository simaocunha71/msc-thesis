```js
const antiShuffle = (s) => {
  // split the string into words
  let words = s.split(' ');
  // for each word in words
  for (let i = 0; i < words.length; i++) {
    // sort the characters in the word and join them back into a string
    words[i] = words[i].split('').sort().join('');
  }
  // join the words back into a string with spaces between them
  return words.join(' ');
}
```

This function takes a string as input and returns a new string where all the words are sorted alphabetically. It splits the input string into an array of words, sorts each word alphabetically, and then joins the words back into a string with spaces between them.