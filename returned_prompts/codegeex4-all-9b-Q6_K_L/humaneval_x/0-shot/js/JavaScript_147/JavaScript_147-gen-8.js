```java
const getMaxTriples = (n) => {
  let a = new Array(n);
  let res = 0;
  for (let i = 0; i < n; i++) {
    a[i] = (i + 1) * (i + 1) - (i + 1) + 1;
  }
  for (let i = 0; i < n - 2; i++) {
    for (let j = i + 1; j < n - 1; j++) {
      for (let k = j + 1; k < n; k++) {
        if ((a[i] + a[j] + a[k]) % 3 === 0) {
          res++;
        }
      }
    }
  }
  return res;
}
```
