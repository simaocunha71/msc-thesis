```java
const howManyTimes = (string, substring) => {
  if (substring.length == 0) return 0;
  let count = 0;
  for (let i = 0; i <= string.length - substring.length; i++) {
    if (string.substring(i, i + substring.length) == substring) count++;
  }
  return count;
}
```
