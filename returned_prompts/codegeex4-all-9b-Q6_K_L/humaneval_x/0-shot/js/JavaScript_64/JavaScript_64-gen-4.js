```java
const vowelsCount = (s) => {
  var s2 = s.toLowerCase();
  var vowels = 'aeiou';
  var count = 0;
  for (const c of s2) {
    if (vowels.includes(c)) {
      count += 1;
    }
  }
  if (s2.endsWith('y')) {
    count += 1;
  }
  return count;
}
```
