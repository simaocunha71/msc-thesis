```java
const tri = (n) => {
  let a = [1, 3, 2];
  for (let i = 3; i <= n; i++) {
    if (i % 2 == 0) {
      a.push(1 + i / 2);
    } else {
      a.push(a[i - 1] + a[i - 2] + a[i + 1]);
    }
  }
  return a;
}
```
