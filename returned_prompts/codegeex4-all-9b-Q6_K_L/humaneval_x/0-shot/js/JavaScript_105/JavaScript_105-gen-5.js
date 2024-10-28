```java
const byLength = (arr) => {
  let temp = []
  for (let i = 0; i < arr.length; i++) {
    if (arr[i] >= 1 && arr[i] <= 9) {
      temp.push(arr[i])
    }
  }
  temp.sort((a, b) => a - b)
  temp.reverse()
  let res = []
  for (let i = 0; i < temp.length; i++) {
    switch (temp[i]) {
      case 1:
        res.push('One')
        break
      case 2:
        res.push('Two')
        break
      case 3:
        res.push('Three')
        break
      case 4:
        res.push('Four')
        break
      case 5:
        res.push('Five')
        break
      case 6:
        res.push('Six')
        break
      case 7:
        res.push('Seven')
        break
      case 8:
        res.push('Eight')
        break
      case 9:
        res.push('Nine')
        break
    }
  }
  return res
}
```
