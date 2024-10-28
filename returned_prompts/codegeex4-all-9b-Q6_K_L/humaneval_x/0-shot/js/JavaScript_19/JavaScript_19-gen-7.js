```java
const sortNumbers = (numbers) => {
  let nums = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'];
  let arr = numbers.split(' ');
  let sorted = arr.sort((a, b) => nums.indexOf(a) - nums.indexOf(b));
  return sorted.join(' ');
}
```
