```java
const solution = (lst) => {
  return lst.filter((e, i) => i % 2 == 0 && e % 2 != 0).reduce((x, y) => x + y, 0);
}
```
