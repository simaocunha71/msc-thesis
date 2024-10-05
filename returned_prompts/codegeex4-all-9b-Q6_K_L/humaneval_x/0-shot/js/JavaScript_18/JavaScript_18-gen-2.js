```java
const howManyTimes = (string, substring) => {
  if (string.length == 0 || substring.length == 0) return 0;
  let count = 0;
  let i = 0;
  while (i <= string.length - substring.length) {
    let j = 0;
    while (j < substring.length && string[i + j] == substring[j]) {
      j++;
    }
    if (j == substring.length) {
      count++;
      i += substring.length;
    } else {
      i++;
    }
  }
  return count;
}
```
