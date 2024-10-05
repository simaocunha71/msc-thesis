```java
const getClosestVowel = (word) => {
  let vowels = 'aeiouAEIOU';
  let res = '';
  for (let i = word.length - 1; i > 0; i--) {
    if (vowels.includes(word[i]) && !vowels.includes(word[i - 1])) {
      res = word[i];
      break;
    }
  }
  return res;
}
```