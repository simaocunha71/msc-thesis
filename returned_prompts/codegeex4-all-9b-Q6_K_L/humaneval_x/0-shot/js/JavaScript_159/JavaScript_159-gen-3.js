```java
const eat = (number, need, remaining) => {
  let eaten = number + need;
  let left = remaining - need;
  if (left < 0) {
    eaten += left;
    left = 0;
  }
  return [eaten, left];
}
```
