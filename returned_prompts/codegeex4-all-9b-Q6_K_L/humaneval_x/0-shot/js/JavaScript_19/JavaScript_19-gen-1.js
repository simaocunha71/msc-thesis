```java
const sortNumbers = (numbers) => {
  let num = numbers.split(' ');
  let sortedNum = num.sort((a,b) => {
    return a - b;
  });
  return sortedNum.join(' ');
}
```
