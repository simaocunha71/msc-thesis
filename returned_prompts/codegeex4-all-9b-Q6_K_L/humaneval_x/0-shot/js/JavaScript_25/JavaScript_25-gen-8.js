```java
const factorize = (n) => {
  var res = [];
  for (let i = 2; i <= Math.sqrt(n); i++) {
    while (n % i == 0) {
      res.push(i);
      n = n / i;
    }
  }
  if (n > 1) {
    res.push(n);
  }
  return res;
}
```