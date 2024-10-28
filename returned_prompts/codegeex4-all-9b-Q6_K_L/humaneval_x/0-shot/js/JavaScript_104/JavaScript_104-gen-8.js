```java
const uniqueDigits = (x) => {
  return x.filter(e => {
    return !String(e).split('').some(d => d % 2 == 0);
  }).sort((a, b) => a - b);
}
```
