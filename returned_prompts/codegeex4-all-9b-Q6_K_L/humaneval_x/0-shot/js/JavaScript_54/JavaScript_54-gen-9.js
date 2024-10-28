```java
const sameChars = (s0, s1) => {
  if (s0.length !== s1.length) {
    return false;
  }
  const charCount = new Map();
  for (let i = 0; i < s0.length; i++) {
    const char0 = s0[i];
    const char1 = s1[i];
    if (char0 !== char1) {
      return false;
    }
    if (!charCount.has(char0)) {
      charCount.set(char0, 0);
    }
    charCount.set(char0, charCount.get(char0) + 1);
  }
  for (const [char, count] of charCount) {
    if (s1.split(char).length - 1 !== count) {
      return false;
    }
  }
  return true;
}
```