```java
const maxElement = (l) => {
  var max = l[0];
  for (let i = 1; i < l.length; i++) {
    if (l[i] > max) {
      max = l[i];
    }
  }
  return max;
}
```