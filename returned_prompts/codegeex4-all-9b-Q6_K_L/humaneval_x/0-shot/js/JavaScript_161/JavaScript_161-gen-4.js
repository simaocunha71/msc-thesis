```java
const solve = (s) => {
  if (!/[a-zA-Z]/.test(s)) {
    return s.split('').reverse().join('');
  }
  let result = '';
  for (let i = 0; i < s.length; i++) {
    if (/[a-z]/.test(s[i])) {
      result += s[i].toUpperCase();
    } else if (/[A-Z]/.test(s[i])) {
      result += s[i].toLowerCase();
    } else {
      result += s[i];
    }
  }
  return result;
}
```
