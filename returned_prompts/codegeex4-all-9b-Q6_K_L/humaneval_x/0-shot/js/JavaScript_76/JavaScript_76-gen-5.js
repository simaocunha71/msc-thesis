```java
const isSimplePower = (x, n) => {
  var i = 2;
  while (i <= x) {
    if (i ** Math.floor(Math.log(x) / Math.log(i)) == x) {
      return true;
    }
    i++;
  }
  return false;
}
```