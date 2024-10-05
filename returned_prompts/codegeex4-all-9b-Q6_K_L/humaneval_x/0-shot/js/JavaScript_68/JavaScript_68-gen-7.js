```java
const pluck = (arr) => {
  if (arr.length === 0) return [];
  let smallest_even = Infinity;
  let smallest_even_index = -1;
  for (let i = 0; i < arr.length; i++) {
    if (arr[i] % 2 === 0 && arr[i] < smallest_even) {
      smallest_even = arr[i];
      smallest_even_index = i;
    }
  }
  if (smallest_even_index === -1) return [];
  return [smallest_even, smallest_even_index];
}
```
