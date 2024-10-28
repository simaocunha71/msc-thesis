```java
const getClosestVowel = (word) => {
  let vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
  let w = word.split('').reverse().join('')
  for (let i = 1; i < w.length - 1; i++) {
    if (vowels.includes(w[i]) && !vowels.includes(w[i + 1]) && !vowels.includes(w[i - 1])) {
      return w[i]
    }
  }
  return ''
}
```
