Here is the solution in JavaScript:
```javascript
const sumSquares = (lst) => {
  let sum = 0;
  for (let i = 0; i < lst.length; i++) {
    if ((i + 1) % 3 === 0 && (i + 1) % 4 !== 0) {
      sum += lst[i] ** 2;
    } else if ((i + 1) % 4 === 0 && (i + 1) % 3 !== 0) {
      sum += lst[i] ** 3;
    } else {
      sum += lst[i];
    }
  }
  return sum;
};
```
Explanation:
The function iterates over the list using a for loop. For each entry, it checks the index (plus 1) to see if it is a multiple of 3 and/or 4. If it is a multiple of 3 but not 4, it squares the entry. If it is a multiple of 4 but not 3, it cubes the entry. If it is neither, it leaves the entry as is. The sum of all entries is then returned. The `**` operator is used for exponentiation (squaring and cubing). The `+ 1` is used to make the indexing 1-based instead of 0-based.