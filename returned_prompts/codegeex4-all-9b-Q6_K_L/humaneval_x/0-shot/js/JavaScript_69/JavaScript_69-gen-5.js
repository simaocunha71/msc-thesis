```java
const search = (lst) => {
  var freqMap = new Map();
  for (let i = 0; i < lst.length; i++) {
    if (freqMap.has(lst[i])) {
      freqMap.set(lst[i], freqMap.get(lst[i]) + 1);
    } else {
      freqMap.set(lst[i], 1);
    }
  }
  let maxFreq = -1;
  for (let [key, value] of freqMap) {
    if (value >= key) {
      maxFreq = Math.max(maxFreq, key);
    }
  }
  return maxFreq;
}
```