```java
const vowelsCount = (s) => {
  let vowels = 'aeiou';
  let count = 0;
  let s2 = s.toLowerCase();
  for (let i = 0; i < s2.length; i++) {
    if (vowels.indexOf(s2[i]) !== -1) {
      count++;
    }
  }
  if (s[s.length - 1].toLowerCase() === 'y') count++;
  return count;
}
```
