```java
const selectWords = (s, n) => {
  var t = s.split(' ');
  var p = ['a', 'e', 'i', 'o', 'u'];
  var q = [];
  for (var i = 0; i < t.length; i++) {
    var c = 0;
    for (var j = 0; j < t[i].length; j++) {
      if (p.indexOf(t[i][j]) === -1) {
        c++;
      }
    }
    if (c === n) {
      q.push(t[i]);
    }
  }
  return q;
}
```