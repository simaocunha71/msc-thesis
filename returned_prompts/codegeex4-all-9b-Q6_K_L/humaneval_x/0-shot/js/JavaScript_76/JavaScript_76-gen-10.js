```java
const isSimplePower = (x, n) => {
  return Math.pow(n, Math.floor(Math.log(x) / Math.log(n))) === x
}
```
