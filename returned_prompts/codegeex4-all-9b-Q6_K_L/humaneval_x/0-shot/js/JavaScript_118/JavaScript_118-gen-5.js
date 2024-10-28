```java
const getClosestVowel = (word) => {
  const vowels = 'AEIOUaeiou'
  for (let i = word.length - 1; i >= 0; i--) {
    if (vowels.includes(word[i]) && i !== 0 && i !== word.length - 1) {
      if (vowels.includes(word[i - 1]) && vowels.includes(word[i + 1])) {
        return word[i]
      }
    }
  }
  return ''
}
```
