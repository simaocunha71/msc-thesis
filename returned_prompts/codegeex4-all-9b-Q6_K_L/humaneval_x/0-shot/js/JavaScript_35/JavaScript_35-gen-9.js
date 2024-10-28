```java
const maxElement = (l) => {
  var max = l[0]
  for (const i of l) {
    if (i > max)
      max = i
  }
  return max
}
```