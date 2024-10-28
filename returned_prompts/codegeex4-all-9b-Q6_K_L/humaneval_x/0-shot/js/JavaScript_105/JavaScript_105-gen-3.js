```java
const byLength = (arr) => {
  let arr2 = []
  for (let i = 0; i < arr.length; i++) {
    if (arr[i] >= 1 && arr[i] <= 9) {
      arr2.push(arr[i])
    }
  }
  arr2.sort((a, b) => a - b)
  arr2.reverse()
  return arr2.map(el => {
    switch (el) {
      case 1:
        return "One"
      case 2:
        return "Two"
      case 3:
        return "Three"
      case 4:
        return "Four"
      case 5:
        return "Five"
      case 6:
        return "Six"
      case 7:
        return "Seven"
      case 8:
        return "Eight"
      case 9:
        return "Nine"
    }
  })
}
```
