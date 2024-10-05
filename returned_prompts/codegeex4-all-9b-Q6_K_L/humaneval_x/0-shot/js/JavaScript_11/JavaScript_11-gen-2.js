```java
const stringXor = (a, b) => {
  let xor = '';
  for (let i = 0; i < a.length; i++) {
    xor += a[i] ^ b[i];
  }
  return xor;
}
```