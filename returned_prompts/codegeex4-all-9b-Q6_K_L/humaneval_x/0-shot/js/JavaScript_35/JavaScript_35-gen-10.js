```java
const maxElement = (l) => {
  if (l.length == 0) {
    throw "List is empty";
  }
  let max = l[0];
  for (let i = 1; i < l.length; i++) {
    if (l[i] > max) {
      max = l[i];
    }
  }
  return max;
}
```