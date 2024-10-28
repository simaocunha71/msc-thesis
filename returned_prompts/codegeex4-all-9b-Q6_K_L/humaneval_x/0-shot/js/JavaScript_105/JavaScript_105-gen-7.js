```java
const byLength = (arr) => {
  let ones = ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine'];
  return arr.sort((a, b) => a - b)
            .reverse()
            .map((e) => ones[e - 1]);
}
```
