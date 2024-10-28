```java
const cycpatternCheck = (a, b) => {
  for (let i = 0; i < b.length; i++) {
    let j = 0;
    let k = i;
    while (j < b.length && a[k] == b[j]) {
      k++;
      j++;
      if (k == a.length) {
        return true;
      }
      if (j == b.length) {
        k = 0;
        j = 0;
      }
    }
  }
  return false;
}
```
