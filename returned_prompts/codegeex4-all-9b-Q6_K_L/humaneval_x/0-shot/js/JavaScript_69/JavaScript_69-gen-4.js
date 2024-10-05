```java
const search = (lst) => {
  let arr = []
  for (let i = 0; i < lst.length; i++) {
    let count = 0
    for (let j = 0; j < lst.length; j++) {
      if (lst[j] === lst[i]) {
        count++
      }
    }
    arr.push(count)
  }
  for (let i = 0; i < arr.length; i++) {
    if (arr[i] >= lst[i]) {
      return lst[i]
    }
  }
  return -1
}
```