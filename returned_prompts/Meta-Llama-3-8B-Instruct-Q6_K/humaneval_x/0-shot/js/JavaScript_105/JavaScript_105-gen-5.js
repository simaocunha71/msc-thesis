Here is a JavaScript solution for the problem:

```javascript
const byLength = (arr) => {
  return arr
    .filter(num => num >= 1 && num <= 9)
    .sort((a, b) => a - b)
    .reverse()
    .map(num => {
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
        default: return '';
      }
    })
    .filter(word => word !== '');
};
```

This function first filters the array to include only numbers between 1 and 9. Then it sorts the array in ascending order and reverses it. Finally, it maps each number to its corresponding word and filters out any empty strings.

For example, if you call `byLength([2, 1, 1, 4, 5, 8, 2, 3])`, the function will return `["Eight", "Five", "Four", "Three", "Two", "Two", "One", "One"]`. If you call `byLength([])`, the function will return an empty array `[]`. If you call `byLength([1, -1, 55])`, the function will return `["One"]`.