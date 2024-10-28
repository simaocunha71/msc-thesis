```java
const monotonic = (l) => {
  if (l.length < 2) return true;
  let increasing = l[0] <= l[1];
  for (let i = 1; i < l.length - 1; i++) {
    if ((l[i] < l[i - 1] && increasing) || (l[i] > l[i - 1] && !increasing)) return false;
  }
  return true;
}
```
