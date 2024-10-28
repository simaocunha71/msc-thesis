```java
const changeBase = (x, base) => {
  let rem = x % base;
  let div = Math.floor(x / base);
  if (div == 0)
    return rem.toString();
  else
    return changeBase(div, base) + rem.toString();
}
```
