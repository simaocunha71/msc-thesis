```java
const howManyTimes = (string, substring) => {
  let count = 0;
  let index = 0;
  while (index < string.length) {
    index = string.indexOf(substring, index);
    if (index === -1) break;
    count++;
    index++;
  }
  return count;
}
```
