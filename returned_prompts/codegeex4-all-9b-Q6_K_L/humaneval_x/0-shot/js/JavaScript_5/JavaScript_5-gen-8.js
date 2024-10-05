```javascript
const intersperse = (numbers, delimeter) => {
  if (numbers.length === 0) return [];
  let result = [numbers[0]];
  for (let i = 1; i < numbers.length; i++) {
    result.push(delimeter, numbers[i]);
  }
  return result;
}
```