```java
const sameChars = (s0, s1) => {
  if (s0.length !== s1.length) return false;
  let arr = new Array(256).fill(0);
  for (let c of s0) {
    arr[c.charCodeAt(0)]++;
  }
  for (let c of s1) {
    arr[c.charCodeAt(0)]--;
    if (arr[c.charCodeAt(0)] < 0) return false;
  }
  return true;
}
```
