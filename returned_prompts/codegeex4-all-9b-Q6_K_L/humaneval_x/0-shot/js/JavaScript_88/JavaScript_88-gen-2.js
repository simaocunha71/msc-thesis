```js
const sortArray = (array) => {
  if (array.length === 0) return [];
  if (array.length === 1) return array;
  
  const sum = array[0] + array[array.length - 1];
  const sortedArray = [...array].sort((a, b) => sum % 2 === 0 ? b - a : a - b);
  
  return sortedArray;
}
```