```java
const changeBase = (x, base) => {
  var rem = 0;
  var s = "";
  while (x > 0) {
    rem = x % base;
    s = rem + s;
    x = Math.floor(x / base);
  }
  return s;
}
```
