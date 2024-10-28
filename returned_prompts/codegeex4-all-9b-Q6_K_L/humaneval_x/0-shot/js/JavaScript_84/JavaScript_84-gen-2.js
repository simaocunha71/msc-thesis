```java
const solve = (N) => {
  return N.toString(2).split('').reduce((a, b) => a + (+b), 0).toString(2)
}
```