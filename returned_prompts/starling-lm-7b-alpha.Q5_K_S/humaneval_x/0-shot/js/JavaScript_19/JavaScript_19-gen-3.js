To solve this problem, you can use the following JavaScript function:

```javascript
const sortNumbers = (numbers) => {
  const nums = numbers.split(' ').map(word => {
    switch (word) {
      case 'zero': return 0;
      case 'one': return 1;
      case 'two': return 2;
      case 'three': return 3;
      case 'four': return 4;