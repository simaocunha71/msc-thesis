```java
const byLength = (arr) => {
  const dic = {
    '1': 'One', '2': 'Two', '3': 'Three', '4': 'Four', '5': 'Five', '6': 'Six', '7': 'Seven', '8': 'Eight', '9': 'Nine'
  };
  return arr
    .filter((num) => num > 0 && num < 10)
    .sort((a, b) => a - b)
    .reverse()
    .map((num) => dic[num]);
}
```
