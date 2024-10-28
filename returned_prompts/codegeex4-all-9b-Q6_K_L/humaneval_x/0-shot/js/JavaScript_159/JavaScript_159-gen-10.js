```java
const eat = (number, need, remaining) => {
  return [need + number, remaining - need < 0 ? 0 : remaining - need]
}
```
