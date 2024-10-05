```java
const hexKey = (num) => {
  let arr = num.split("");
  let prime = ['2', '3', '5', '7', 'B', 'D'];
  let count = 0;
  for (let i = 0; i < arr.length; i++) {
    if (prime.includes(arr[i])) {
      count++;
    }
  }
  return count;
}
```
