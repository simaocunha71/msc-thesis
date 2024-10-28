```java
const moveOneBall = (arr) => {
  if (arr.length == 0) return true;
  let min = Math.min(...arr);
  for (let i = 0; i < arr.length; i++) {
    if (arr[i] == min) {
      arr = arr.slice(i).concat(arr.slice(0, i));
      break;
    }
  }
  for (let i = 1; i < arr.length; i++) {
    if (arr[i] < arr[i - 1]) {
      return false;
    }
  }
  return true;
}
```
