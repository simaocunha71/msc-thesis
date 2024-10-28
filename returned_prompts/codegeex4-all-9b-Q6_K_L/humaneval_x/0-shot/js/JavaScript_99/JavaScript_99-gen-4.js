```java
const closestInteger = (value) => {
  let val = Math.round(parseFloat(value))
  if (val < 0) {
    return Math.floor(val)
  } else {
    return Math.ceil(val)
  }
}
```
