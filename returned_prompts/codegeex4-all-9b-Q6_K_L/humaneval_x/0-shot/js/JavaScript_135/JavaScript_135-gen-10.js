```java
const canArrange = (arr) => {
  if (arr.length <= 1) return -1;
  for (let i = 1; i < arr.length; i++) {
    if (arr[i] < arr[i - 1]) return i - 1;
  }
  return -1;
}
```