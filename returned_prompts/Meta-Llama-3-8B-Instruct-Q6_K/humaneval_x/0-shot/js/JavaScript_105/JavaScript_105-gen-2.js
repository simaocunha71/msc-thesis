Here is the solution:

```javascript
const byLength = (arr) => {
  const oneToNine = arr.filter(num => num >= 1 && num <= 9);
  const sortedOneToNine = oneToNine.sort((a, b) => a - b);
  const reversedSortedOneToNine = sortedOneToNine.reverse();
  return reversedSortedOneToNine.map(num => {
    switch (num) {
      case 1: return "One";
      case 2: return "Two";
      case 3: return "Three";
      case 4: return "Four";
      case 5: return "Five";
      case 6: return "Six";
      case 7: return "Seven";
      case 8: return "Eight";
      case 9: return "Nine";
      default: return "";
    }
  });
};
```


Explanation:
This function first filters out the numbers between 1 and 9 from the input array. It then sorts these numbers in ascending order and reverses the sorted array. Finally, it maps each number in the reversed array to its corresponding name (e.g., 1 becomes "One") using a switch statement. The function returns the array of names. If the input array is empty, it returns an empty array. If the array has any numbers outside the range of 1 to 9, they are ignored and not included in the output array.