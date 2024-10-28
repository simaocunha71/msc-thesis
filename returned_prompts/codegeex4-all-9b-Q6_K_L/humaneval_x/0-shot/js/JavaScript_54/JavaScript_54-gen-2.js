```java
const sameChars = (s0, s1) => {
  if (s0.length != s1.length) return false;
  let count = new Array(256).fill(0);
  for (let i = 0; i < s0.length; i++) {
    count[s0.charCodeAt(i)]++;
    count[s1.charCodeAt(i)]--;
  }
  for (let i = 0; i < 256; i++) {
    if (count[i] != 0) return false;
  }
  return true;
}
```