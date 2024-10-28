```java
const byLength = (arr) => {
  if (!Array.isArray(arr) || arr.length == 0) return []
  let nums = []
  for (let i = 0; i < arr.length; i++) {
    if (arr[i] >= 1 && arr[i] <= 9) {
      nums.push(arr[i])
    }
  }
  nums.sort((a, b) => a - b)
  nums.reverse()
  let dict = {
    1: 'One',
    2: 'Two',
    3: 'Three',
    4: 'Four',
    5: 'Five',
    6: 'Six',
    7: 'Seven',
    8: 'Eight',
    9: 'Nine'
  }
  return nums.map(x => dict[x])
}
```
