```java
const moveOneBall = (arr) => {
  if (arr.length === 0) return true;
  let min = arr[0], max = arr[0];
  for (let i = 0; i < arr.length; i++) {
    if (arr[i] < min) min = arr[i];
    if (arr[i] > max) max = arr[i];
  }
  let sorted = arr.slice().sort((a, b) => a - b);
  let shift = 0;
  while (shift < arr.length) {
    if (arr[shift] === min) break;
    shift++;
  }
  for (let i = 0; i < arr.length - shift; i++) {
    if (arr[i] !== sorted[i]) return false;
  }
  for (let i = arr.length - shift; i < arr.length; i++) {
    if (arr[i] !== sorted[i - (arr.length - shift)]) return false;
  }
  return true;
}
```
