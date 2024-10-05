```java
const closestInteger = (value) => {
  let num = Number(value);
  let floored = Math.floor(num);
  let ceiled = Math.ceil(num);
  if (num - floored < ceiled - num) {
    return floored;
  } else {
    return ceiled;
  }
}
```
