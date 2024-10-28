```java
const sameChars = (s0, s1) => {
  if (s0.length !== s1.length) return false;
  const count = {};
  for (const c of s0) {
    count[c] = (count[c] || 0) + 1;
  }
  for (const c of s1) {
    if (!count[c]) return false;
    count[c]--;
  }
  return true;
}
```