```javascript
const sortArray = (array) => {
  if (array.length <= 1) return array;
  const sortedArray = array.slice().sort((a, b) => a - b);
  const sum = array[0] + array[array.length - 1];
  return sum % 2 === 0 ? sortedArray.reverse() : sortedArray;
}
```