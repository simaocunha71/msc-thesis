```java
const rightAngleTriangle = (a, b, c) => {
  var sides = [a, b, c].sort((a, b) => b - a);
  return Math.pow(sides[0], 2) === Math.pow(sides[1], 2) + Math.pow(sides[2], 2);
}
```
