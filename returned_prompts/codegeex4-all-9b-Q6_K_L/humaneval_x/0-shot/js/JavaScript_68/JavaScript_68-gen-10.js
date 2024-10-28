```java
const pluck = (arr) => {
  var smallest_even = [Infinity, -1];
  for (let i = 0; i < arr.length; i++) {
    if (arr[i] % 2 === 0 && arr[i] < smallest_even[0]) {
      smallest_even = [arr[i], i];
    }
  }
  return smallest_even[0] === Infinity ? [] : smallest_even;
}
```
