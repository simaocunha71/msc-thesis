```java
const selectWords = (s, n) => {
  const words = s.split(' ');
  const result = [];
  for (const word of words) {
    const consonants = word.match(/[bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ]/g);
    if (consonants && consonants.length === n) {
      result.push(word);
    }
  }
  return result;
}
```
