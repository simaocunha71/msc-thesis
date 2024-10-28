Here is the solution to the problem:

```javascript
const removeVowels = (text) => {
  const vowels = 'aeiou';
  return text.split('').filter((char) => !vowels.includes(char)).join('');
}
```
This function works by splitting the text into an array of characters, filtering out any characters that are vowels, and then joining the remaining characters back together into a string.