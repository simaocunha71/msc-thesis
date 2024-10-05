```java
const moveOneBall = (arr) => {
  if (arr.length === 0) return true;
  let minIndex = 0;
  for (let i = 1; i < arr.length; i++) {
    if (arr[i] < arr[minIndex]) {
      minIndex = i;
    }
  }
  let count = 0;
  for (let i = minIndex + 1; i < arr.length; i++) {
    if (arr[i] < arr[i - 1]) {
      count++;
    }
  }
  for (let i = 0; i < minIndex; i++) {
    if (arr[i] > arr[i + 1]) {
      count++;
    }
  }
  return count <= 1;
}
```
