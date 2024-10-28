```java
const reverseDelete = (s, c) => {
  let t = '';
  for (let i = 0; i < s.length; i++) {
    if (c.indexOf(s[i]) == -1) {
      t += s[i];
    }
  }
  if (t == t.split('').reverse().join('')) {
    return [t, true];
  } else {
    return [t, false];
  }
}
```
