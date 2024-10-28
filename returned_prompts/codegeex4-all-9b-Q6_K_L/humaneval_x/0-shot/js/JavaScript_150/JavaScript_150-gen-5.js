```java
const xOrY = (n, x, y) => {
  var is_prime = function (num) {
    if (num <= 1) return false;
    for (var i = 2; i < num; i++) {
      if (num % i === 0) return false;
    }
    return true;
  }
  return is_prime(n) ? x : y;
}
```
