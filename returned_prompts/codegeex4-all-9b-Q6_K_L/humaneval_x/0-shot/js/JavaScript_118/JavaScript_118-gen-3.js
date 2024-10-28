```java
const getClosestVowel = (word) => {
  let vowels = 'aeiouAEIOU';
  let i = word.length - 1;
  while (i > 0) {
    if (vowels.includes(word[i])) {
      if (vowels.includes(word[i - 1]) || vowels.includes(word[i + 1])) {
        return word[i];
      }
    }
    i--;
  }
  return "";
}
```
