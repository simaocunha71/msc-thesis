```java
const search = (lst) => {
  var frequency = {};
  lst.forEach(el => {
    if (frequency[el]) {
      frequency[el]++;
    } else {
      frequency[el] = 1;
    }
  });
  var max = -1;
  for (var el in frequency) {
    if (frequency[el] >= el) {
      max = Math.max(max, el);
    }
  }
  return max;
}
```