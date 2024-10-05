```java
const rightAngleTriangle = (a, b, c) => {
  let sides = [a, b, c]
  sides.sort((a, b) => a - b)
  return sides[0] ** 2 + sides[1] ** 2 === sides[2] ** 2
}
```
