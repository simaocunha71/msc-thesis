```
function byLength(arr) {
  const validNumbers = arr.filter(num => 1 <= num && num <= 9);
  const sortedValidNumbers = validNumbers.sort((a, b) => a - b);
  const reversedSortedValidNumbers = sortedValidNumbers.reverse();
  return reversedSortedValidNumbers.map(num => {
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
}
```  