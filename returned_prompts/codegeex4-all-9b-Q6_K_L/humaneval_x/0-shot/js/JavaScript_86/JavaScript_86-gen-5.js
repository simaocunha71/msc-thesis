```javascript
const antiShuffle = (s) => {
  // Split the string into words
  const words = s.split(' ');

  // Sort each word by ASCII values
  const sortedWords = words.map(word => word.split('').sort().join(''));

  // Join the sorted words back into a string
  return sortedWords.join(' ');
}
```
