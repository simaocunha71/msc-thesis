```java
const closestInteger = (value) => {
  value = Number(value)
  if (value < 0) {
    return Math.floor(value)
  } else {
    return Math.ceil(value)
  }
}
```
