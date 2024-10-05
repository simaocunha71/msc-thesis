```java
const encrypt = (s) => {
  let e = '';
  for (let i = 0; i < s.length; i++) {
    let c = s[i].charCodeAt(0);
    if (c >= 65 && c <= 90) {
      c = ((c - 65) * 2 + 2) % 26 + 65;
    } else if (c >= 97 && c <= 122) {
      c = ((c - 97) * 2 + 2) % 26 + 97;
    }
    e += String.fromCharCode(c);
  }
  return e;
}
```