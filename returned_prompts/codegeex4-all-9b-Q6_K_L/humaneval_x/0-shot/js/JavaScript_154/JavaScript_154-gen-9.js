```java
const cycpatternCheck = (a, b) => {
  let n = b.length;
  let m = a.length;
  for (let i = 0; i < n; i++) {
    let j = 0;
    while (j < n && a[i + j] == b[j]) {
      j++;
    }
    if (j == n) {
      return true;
    }
    if (i + j < m) {
      let k = i + j;
      while (k < m - j && a[k] == b[0]) {
        k++;
      }
      if (k == m - j) {
        return true;
      }
    }
  }
  return false;
}
```
