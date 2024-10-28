Here is the solution in JavaScript:

```javascript
const oddCount = (lst) => {
  return lst.map(str => {
    let numOdds = 0;
    for (let i = 0; i < str.length; i++) {
      if (parseInt(str[i]) % 2 !== 0) {
        numOdds++;
      }
    }
    return `the number of odd elements ${numOdds}n the str${numOdds}ng ${numOdds} of the ${numOdds}nput.`;
  });
};
```

Explanation:

The `map` function is used to iterate over each string in the list. For each string, we initialize a counter `numOdds` to 0. We then iterate over each character in the string, and if the character is an odd number (i.e. `parseInt(str[i]) % 2 !== 0`), we increment `numOdds` by 1. Finally, we return a string that includes the number of odd elements and the corresponding string and input numbers.