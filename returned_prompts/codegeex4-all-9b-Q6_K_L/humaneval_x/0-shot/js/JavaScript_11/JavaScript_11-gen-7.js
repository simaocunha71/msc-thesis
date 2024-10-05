```java
const stringXor = (a, b) => {
  let c = '';
  for (let i = 0; i < a.length; i++) {
    c += a[i] ^ b[i];
  }
  return c;
}
```
