```java
const byLength = (arr) => {
  let ret = []
  const dic = {
    '1': 'One',
    '2': 'Two',
    '3': 'Three',
    '4': 'Four',
    '5': 'Five',
    '6': 'Six',
    '7': 'Seven',
    '8': 'Eight',
    '9': 'Nine'
  }
  for (let i = 0; i < arr.length; i++) {
    if (arr[i] >= 1 && arr[i] <= 9) {
      ret.push(dic[arr[i].toString()])
    }
  }
  ret.sort((a, b) => a.length - b.length)
  ret.reverse()
  return ret
}
```
