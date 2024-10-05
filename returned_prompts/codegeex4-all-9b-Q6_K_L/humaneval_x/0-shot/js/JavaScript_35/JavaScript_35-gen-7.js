```java
const maxElement = (l) => {
  var max = -Infinity;
  for (let i = 0; i < l.length; i++) {
    if (l[i] > max) {
      max = l[i];
    }
  }
  return max;
}
```