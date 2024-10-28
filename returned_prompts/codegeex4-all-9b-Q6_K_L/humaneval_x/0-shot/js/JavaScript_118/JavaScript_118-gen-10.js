```java
const getClosestVowel = (word) => {
  const vowels = 'AEIOUaeiou';
  let result = '';
  for (let i = word.length - 1; i >= 0; i--) {
    if (vowels.includes(word[i]) && !vowels.includes(word[i - 1]) && !vowels.includes(word[i + 1])) {
      result = word[i];
      break;
    }
  }
  return result;
}
```
