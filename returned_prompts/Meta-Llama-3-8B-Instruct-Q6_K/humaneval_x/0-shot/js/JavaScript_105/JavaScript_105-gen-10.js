Here is a JavaScript solution for the problem:

```javascript
const byLength = (arr) => {
  // Filter the array to include only numbers between 1 and 9
  const filteredArr = arr.filter(num => num >= 1 && num <= 9);
  
  // Sort the filtered array
  filteredArr.sort((a, b) => a - b);
  
  // Reverse the sorted array
  filteredArr = filteredArr.reverse();
  
  // Map the array to replace each digit with its corresponding name
  const result = filteredArr.map(num => {
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
      default: return ''; // Return an empty string for any other number
    }
  });
  
  return result;
};
```

You can test the function with the examples you provided:

```javascript
console.log(byLength([2, 1, 1, 4, 5, 8, 2, 3])); // Output: ["Eight", "Five", "Four", "Three", "Two", "Two", "One", "One"]
console.log(byLength([])); // Output: []
console.log(byLength([1, -1, 55])); // Output: ["One"]
```

This function first filters the array to include only numbers between 1 and 9, then sorts and reverses the array, and finally maps the array to replace each digit with its corresponding name. If the array has any numbers outside the range of 1 to 9, they will be ignored. If the array is empty, the function will return an empty array. If the array has any other numbers, they will be replaced with an empty string.