```java
const sortNumbers = (numbers) => {
  var dic = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9};
  var array = numbers.split(' ');
  array.sort((a, b) => dic[a] - dic[b]);
  return array.join(' ');
}
```
