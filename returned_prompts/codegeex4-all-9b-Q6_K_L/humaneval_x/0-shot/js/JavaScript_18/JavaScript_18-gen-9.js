```java
const howManyTimes = (string, substring) => {
  let count = 0;
  for (let i = 0; i <= string.length - substring.length; i++) {
    if (string.substring(i, i + substring.length) === substring) {
      count++;
      i += substring.length - 1;
    }
  }
  return count;
}
```
