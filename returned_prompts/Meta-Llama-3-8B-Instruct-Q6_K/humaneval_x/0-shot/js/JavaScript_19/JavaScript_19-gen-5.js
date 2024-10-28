```javascript
const numbers = 'three one five'.split(' ');
const sortedNumbers = numbers.sort((a, b) => {
  const numMap = {
    zero: 0,
    one: 1,
    two: 2,
    three: 3,
    four: 4,
    five: 5,
    six: 6,
    seven: 7,
    eight: 8,
    nine: 9
  };
  return numMap[a] - numMap[b];
});
return sortedNumbers.join(' ');
```
In this solution, we first split the input string into an array of numbers using the `split` method. Then we sort this array using the `sort` method and a custom comparison function. This comparison function uses an object `numMap` to map the string representations of numbers to their integer values. The `sort` method then compares these integer values to determine the correct order for the array. Finally, we join the sorted array back into a string using the `join` method. The resulting string is the input string with the numbers sorted from smallest to largest. For example, if the input is 'three one five', the output will be 'one three five'.