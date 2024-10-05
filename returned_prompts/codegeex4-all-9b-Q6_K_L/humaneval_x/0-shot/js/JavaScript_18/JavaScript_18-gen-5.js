```java
const howManyTimes = (string, substring) => {
  return (string.match(new RegExp(substring, 'g')) || []).length;
}
```
