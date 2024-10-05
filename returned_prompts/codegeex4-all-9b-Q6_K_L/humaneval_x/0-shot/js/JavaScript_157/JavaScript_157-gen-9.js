```java
const rightAngleTriangle = (a, b, c) => {
  var sides = [a, b, c];
  sides.sort((a, b) => a - b);
  var [a, b, c] = sides;
  return a * a + b * b == c * c;
}
```
