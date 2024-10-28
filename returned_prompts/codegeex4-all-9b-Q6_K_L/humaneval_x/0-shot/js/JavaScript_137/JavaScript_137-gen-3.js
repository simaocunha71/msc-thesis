```java
const compareOne = (a, b) => {
  if (a == b) return null
  if (typeof a == 'string') a = a.replace(',', '.')
  if (typeof b == 'string') b = b.replace(',', '.')
  if (parseFloat(a) > parseFloat(b)) return a
  return b
}
```