Here is the solution in JavaScript:
```
const byLength = (arr) => {
  // Filter the array to include only numbers between 1 and 9
  const filteredArr = arr.filter(num => num >= 1 && num <= 9);
  
  // Sort the filtered array
  filteredArr.sort((a, b) => a - b);
  
  // Reverse the sorted array
  filteredArr = filteredArr.reverse();
  
  // Map the array to its corresponding names
  return filteredArr.map(num => {
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
  }).filter(name => name !== '');
};
```
Here's an explanation of the code:

1. We first filter the array to include only numbers between 1 and 9 using the `filter()` method.
2. We then sort the filtered array using the `sort()` method.
3. We reverse the sorted array using the `reverse()` method.
4. We map the array to its corresponding names using the `map()` method. We use a `switch` statement to determine the name for each number.
5. We filter the resulting array to remove any empty strings that may have been returned if the input array contained numbers outside the range 1-9.

You can test this function with the examples you provided:
```
console.log(byLength([2, 1, 1, 4, 5, 8, 2, 3])); // Output: ["Eight", "Five", "Four", "Three", "Two", "Two", "One", "One"]
console.log(byLength([])); // Output: []
console.log(byLength([1, -1, 55])); // Output: ["One"]
``` 