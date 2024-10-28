```java
const getClosestVowel = (word) => {
  let vowels = 'AEIOUaeiou';
  let len = word.length;
  for (let i = len - 2; i >= 1; i--) {
    if (vowels.includes(word[i]) && !vowels.includes(word[i - 1]) && !vowels.includes(word[i + 1])) {
      return word[i];
    }
  }
  return '';
}
```
