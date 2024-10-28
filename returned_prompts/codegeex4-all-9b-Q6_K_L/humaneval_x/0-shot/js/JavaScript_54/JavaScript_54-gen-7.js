```java
const sameChars = (s0, s1) => {
  if (s0.length != s1.length) return false;
  let m = new Map();
  for (let i = 0; i < s0.length; i++) {
    let c0 = s0.charAt(i);
    let c1 = s1.charAt(i);
    if (c0 != c1) return false;
    if (m.has(c0)) {
      m.set(c0, m.get(c0) + 1);
    } else {
      m.set(c0, 1);
    }
  }
  return true;
}
```