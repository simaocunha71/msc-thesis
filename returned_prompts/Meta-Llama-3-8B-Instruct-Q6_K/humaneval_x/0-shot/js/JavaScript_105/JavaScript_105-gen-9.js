Here is a JavaScript function that solves the problem:

```javascript
const byLength = (arr) => {
  if (!arr.length) return [];
  const sortedArr = arr.filter(num => num >= 1 && num <= 9).sort((a, b) => a - b).reverse();
  return sortedArr.map(num => {
    switch (num) {
      case 1: return 'One';
      case 2: return 'Two';
      case 3: return 'Three';
      case 4: return 'Four';
      case 5: return 'Five';
      case 6: return 'Six';
      case 7: return 'Seven';
      case 8: return 'Eight';
      case 9: return 'Nine';
    }
  });
};
```

This function first filters the array to only include numbers between 1 and 9, sorts the resulting array in ascending order, then reverses it. It then maps the sorted array to an array of strings, where each string is the name of the corresponding digit. If the input array is empty, the function returns an empty array. If the array contains any numbers outside the range 1-9, they are ignored.