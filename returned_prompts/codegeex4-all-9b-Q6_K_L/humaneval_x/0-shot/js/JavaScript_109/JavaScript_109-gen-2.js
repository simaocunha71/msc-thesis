```java
const moveOneBall = (arr) => {
  if (arr.length == 0) return true;
  let min = arr[0];
  let min_index = 0;
  for (let i = 1; i < arr.length; i++) {
    if (arr[i] < min) {
      min = arr[i];
      min_index = i;
    }
  }
  let sorted = true;
  for (let i = 0; i < arr.length - 1; i++) {
    if (arr[(i + min_index) % arr.length] > arr[(i + min_index + 1) % arr.length]) {
      sorted = false;
      break;
    }
  }
  return sorted;
}
```
