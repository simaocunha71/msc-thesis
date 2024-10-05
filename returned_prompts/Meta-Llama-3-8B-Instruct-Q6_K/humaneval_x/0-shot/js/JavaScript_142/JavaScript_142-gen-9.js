```
const sumSquares = (lst) => {
  let sum = 0;
  for (let i = 0; i < lst.length; i++) {
    if ((i + 1) % 3 === 0 && (i + 1) % 4 !== 0) {
      sum += lst[i] ** 2; // square the number
    } else if ((i + 1) % 4 === 0 && (i + 1) % 3 !== 0) {
      sum += lst[i] ** 3; // cube the number
    } else {
      sum += lst[i]; // leave the number as it is
    }
  }
  return sum;
};
```


Explanation:

The function `sumSquares` takes a list of integers as input. It initializes a variable `sum` to 0, which will store the sum of all squared, cubed or original numbers in the list.

The function then iterates over the list using a `for` loop. For each entry in the list, it checks two conditions:

- If the index is a multiple of 3 (i.e., `(i + 1) % 3 === 0`) and not a multiple of 4 (i.e., `(i + 1) % 4 !== 0`), it squares the number and adds it to the sum.
- If the index is a multiple of 4 (i.e., `(i + 1) % 4 === 0`) and not a multiple of 3 (i.e., `(i + 1) % 3 !== 0`), it cubes the number and adds it to the sum.
- If the index is not a multiple of 3 or 4, it leaves the number as it is and adds it to the sum.

Finally, the function returns the sum of all entries in the list.