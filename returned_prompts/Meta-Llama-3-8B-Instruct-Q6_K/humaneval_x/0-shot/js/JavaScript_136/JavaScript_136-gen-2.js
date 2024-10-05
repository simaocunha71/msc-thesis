Here is the solution:

```javascript
const largestSmallestIntegers = (lst) => {
  if (!lst.length) return [null, null];
  
  let negative = null;
  let positive = null;
  
  lst.forEach(num => {
    if (num < 0) {
      if (negative === null || num > negative) {
        negative = num;
      }
    } else if (num > 0) {
      if (positive === null || num < positive) {
        positive = num;
      }
    }
  });
  
  if (negative === null) return [null, positive];
  if (positive === null) return [negative, null];
  
  return [negative, positive];
};
``` 