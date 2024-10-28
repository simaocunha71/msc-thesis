```java
const xOrY = (n, x, y) => {
  var is_prime = true;
  if (n == 1) is_prime = false;
  for (var i = 2; i < n; i++) {
    if (n % i == 0) {
      is_prime = false;
      break;
    }
  }
  if (is_prime) return x;
  else return y;
}
```
