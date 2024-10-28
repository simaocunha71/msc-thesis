```java
const factorize = (n) => {
  var f = []
  for (let i = 2; i <= n; i++) {
    while (n % i == 0) {
      f.push(i)
      n /= i
    }
  }
  return f
}
```