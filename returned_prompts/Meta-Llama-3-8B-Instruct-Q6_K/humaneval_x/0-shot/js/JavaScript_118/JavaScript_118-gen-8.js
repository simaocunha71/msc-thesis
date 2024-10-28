Here is the JavaScript solution for the problem:

```javascript
const getClosestVowel = (word) => {
  let result = '';
  for (let i = word.length - 1; i > 0; i--) {
    if (['a', 'e', 'i', 'o', 'u'].includes(word[i].toLowerCase())) {
      result = word[i];
      break;
    }
  }
  return result;
};
```
This function iterates over the word from right to left (using a for loop). It checks each character to see if it's a vowel (using the includes method with an array of vowel characters). If it finds a vowel, it assigns that vowel to the result variable and breaks out of the loop. If it doesn't find a vowel, the result variable will remain an empty string. Finally, it returns the result. 

Note: This function is case-insensitive for vowels. It converts each character to lowercase before checking if it's a vowel. This means it will treat 'A' and 'a' as the same vowel. If you want a case-sensitive solution, you can remove the toLowerCase() method. 