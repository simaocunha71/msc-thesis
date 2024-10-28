```java
const tri = (n) => {
  let list = [1, 3]
  if (n == 0) return [1]
  if (n == 1) return [1, 3]
  if (n == 2) return [1, 3, 2]
  for (let i = 2; i <= n; i++) {
    if (i % 2 == 0) {
      list.push(1 + i / 2)
    } else {
      list.push(list[i - 1] + list[i - 2] + list[i + 1])
    }
  }
  return list
}
```