```java
const uniqueDigits = (x) => {
  return x.filter(el => {
    return !String(el).split('').some(e => Number(e) % 2 == 0);
  }).sort((a, b) => a - b);
}
```