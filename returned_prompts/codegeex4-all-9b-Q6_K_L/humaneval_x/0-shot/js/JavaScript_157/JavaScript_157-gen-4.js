```java
const rightAngleTriangle = (a, b, c) => {
  var s = a + b + c;
  var p = s / 2;
  var area = Math.sqrt(p * ((p - a) * (p - b) * (p - c)));
  return area == 0;
}
```
