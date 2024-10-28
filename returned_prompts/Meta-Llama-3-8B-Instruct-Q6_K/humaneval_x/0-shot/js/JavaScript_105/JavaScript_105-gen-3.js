Here is a JavaScript function that solves the problem:

```javascript
const byLength = (arr) => {
  const oneToNine = arr.filter(num => num >= 1 && num <= 9);
  const sorted = oneToNine.sort((a, b) => a - b);
  const reversed = sorted.reverse();
  return reversed.map(num => {
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
This function first filters the array to include only numbers between 1 and 9 inclusive. It then sorts these numbers and reverses the sorted array. Finally, it maps each number in the reversed array to its corresponding name using a switch statement. If a number is outside the range of 1 to 9, it is ignored and an empty string is returned. If the input array is empty, an empty array is returned. 