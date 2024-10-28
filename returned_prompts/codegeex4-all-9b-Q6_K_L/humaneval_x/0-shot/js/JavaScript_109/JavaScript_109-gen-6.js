```java
const moveOneBall = (arr) => {
  if (arr.length === 0) {
    return true;
  }
  let min = arr[0];
  let minIndex = 0;
  for (let i = 1; i < arr.length; i++) {
    if (arr[i] < min) {
      min = arr[i];
      minIndex = i;
    }
  }
  let sortedArr = [...arr];
  sortedArr.sort((a, b) => a - b);
  for (let i = 0; i < arr.length; i++) {
    if (sortedArr[i] !== arr[(minIndex + i) % arr.length]) {
      return false;
    }
  }
  return true;
}
```
