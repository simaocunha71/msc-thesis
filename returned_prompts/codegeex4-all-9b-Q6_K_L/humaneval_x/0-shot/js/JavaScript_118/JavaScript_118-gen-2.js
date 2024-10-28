```java
const getClosestVowel = (word) => {
  let vowels = 'aeiouAEIOU'
  for (let i = word.length - 1; i >= 0; i--) {
    if (vowels.includes(word[i]) && !vowels.includes(word[i - 1]) && !vowels.includes(word[i + 1])) {
      return word[i]
    }
  }
  return ''
}
```
