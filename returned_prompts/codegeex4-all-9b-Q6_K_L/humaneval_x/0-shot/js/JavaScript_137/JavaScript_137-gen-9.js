```java
const compareOne = (a, b) => {
  if (a == b) {
    return null
  }
  if (a > b) {
    if (typeof a == 'string') {
      let arr = a.split(',')
      return arr[0] + '.' + arr[1]
    }
    return a
  } else {
    if (typeof b == 'string') {
      let arr = b.split(',')
      return arr[0] + '.' + arr[1]
    }
    return b
  }
}
```
