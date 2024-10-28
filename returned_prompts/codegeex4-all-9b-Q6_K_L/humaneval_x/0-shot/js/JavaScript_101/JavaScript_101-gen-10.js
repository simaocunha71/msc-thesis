```java
const wordsString = (s) => {
  if (s == '') return [];
  var t = s.split(/[\s,]+/);
  for (let i = 0; i < t.length; i++) {
    if (t[i] == '') {
      t.splice(i, 1);
      i--;
    }
  }
  return t;
}
```