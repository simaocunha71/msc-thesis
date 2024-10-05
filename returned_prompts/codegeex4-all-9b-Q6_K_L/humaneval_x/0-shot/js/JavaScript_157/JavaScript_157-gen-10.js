```java
const rightAngleTriangle = (a, b, c) => {
  const sides = [a, b, c].sort((x, y) => x - y);
  return Math.pow(sides[0], 2) + Math.pow(sides[1], 2) == Math.pow(sides[2], 2);
}
```
