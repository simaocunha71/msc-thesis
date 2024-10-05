```javascript
const solution = (lst) => {
  let sum = 0;
  for (let i = 0; i < lst.length; i++) {
    if (i % 2 === 0 && lst[i] % 2 !== 0) {
      sum += lst[i];
    }
  }
  return sum;
};
```


Explanation:
The function `solution` takes a list of integers as an argument. It initializes a variable `sum` to 0, which will be used to store the sum of the odd elements at even positions.

The function then iterates over the list using a `for` loop. For each element at index `i`, it checks two conditions:

1. `i % 2 === 0`: This checks if the index `i` is even (i.e., the element is at an even position).
2. `lst[i] % 2 !== 0`: This checks if the element at index `i` is odd.

If both conditions are true, it means the element is at an even position and is odd. In that case, the element is added to the `sum`.

Finally, the function returns the `sum` after the loop finishes. The `solution` function is then called with the test cases to verify the results.