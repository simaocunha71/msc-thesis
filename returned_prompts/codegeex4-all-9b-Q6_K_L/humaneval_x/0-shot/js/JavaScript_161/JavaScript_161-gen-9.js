```java
const solve = (s) => {
  let t = 0;
  let f = 0;
  for (let i = 0; i < s.length; i++) {
    if (s[i] >= 'a' && s[i] <= 'z') {
      t++;
    }
    else if (s[i] >= 'A' && s[i] <= 'Z') {
      f++;
    }
  }
  if (t == 0 && f == 0) {
    return s.split('').reverse().join('');
  }
  for (let i = 0; i < s.length; i++) {
    if (s[i] >= 'a' && s[i] <= 'z') {
      s = s.substr(0, i) + s[i].toUpperCase() + s.substr(i + 1, s.length - i - 1);
    }
    else if (s[i] >= 'A' && s[i] <= 'Z') {
      s = s.substr(0, i) + s[i].toLowerCase() + s.substr(i + 1, s.length - i - 1);
    }
  }
  return s;
}
```
