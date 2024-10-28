```
const byLength = (arr) => {
  const oneToNine = arr.filter(num => num >= 1 && num <= 9);
  const sortedAndReversed = oneToNine.slice().sort((a, b) => a - b).reverse();
  return sortedAndReversed.map(num => {
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
  }).filter(num => num !== '');
};
``` 

Explanation:

1. First, we filter the array to get only the numbers between 1 and 9 inclusive.
2. Then, we sort the filtered array in ascending order and reverse it.
3. We use the `map` method to convert each number to its corresponding name. We use a `switch` statement to achieve this.
4. Finally, we use the `filter` method to remove any empty strings that might have been returned if the array had any numbers outside the range of 1 to 9. 
5. We return the resulting array of names. If the input array is empty, we return an empty array. If the array has any numbers outside the range of 1 to 9, they are ignored and not included in the output. 

This function should work correctly for the given examples and any other valid input. It also handles the edge cases where the input array is empty or has numbers outside the range of 1 to 9. 