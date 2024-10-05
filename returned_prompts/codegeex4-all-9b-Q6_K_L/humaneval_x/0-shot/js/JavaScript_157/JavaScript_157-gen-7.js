```java
const rightAngleTriangle = (a, b, c) => {
  if (a < b + c && b < a + c && c < a + b) {
    if (a * a == b * b + c * c || b * b == a * a + c * c || c * c == a * a + b * b) {
      return true;
    } else {
      return false;
    }
  } else {
    return false;
  }
}
```
