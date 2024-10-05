```java
const roundedAvg = (n, m) => {
  if (n > m) {
    return -1;
  } else {
    let avg = Math.round((n + m) / 2);
    return "0b" + avg.toString(2);
  }
}
```