```java
const sortNumbers = (numbers) => {
  return numbers.split(' ')
               .filter(n => ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'].includes(n))
               .sort((a, b) => Number(['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'].indexOf(a)) - Number(['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'].indexOf(b)))
               .join(' ');
}
```
