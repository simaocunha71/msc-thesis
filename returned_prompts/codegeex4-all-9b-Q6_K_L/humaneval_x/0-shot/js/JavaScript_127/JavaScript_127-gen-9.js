```java
const intersection = (interval1, interval2) => {
  let s = Math.max(interval1[0], interval2[0])
  let e = Math.min(interval1[1], interval2[1])
  if (s <= e) {
    let l = e - s + 1
    if (l < 2) return 'NO'
    for (let i = 2; i <= Math.sqrt(l); i++) {
      if (l % i == 0) return 'NO'
    }
    return 'YES'
  }
  return 'NO'
}
```
