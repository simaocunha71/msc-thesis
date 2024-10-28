```javascript
const add = (lst) => lst.filter((x, i) => i % 2 !== 0 && x % 2 === 0).reduce((a, b) => a + b, 0);
```


Explanation:

*   `filter()` method is used to create a new array with the elements that pass the test implemented by the provided function.
*   The test function `(x, i) => i % 2 !== 0 && x % 2 === 0` checks if the index is odd (`i % 2 !== 0`) and the element is even (`x % 2 === 0`).
*   The `reduce()` method is used to sum up the even elements at odd indices.
*   The initial value of the accumulator `a` is set to 0, so the sum starts from 0.
*   The function returns the sum of the even elements at odd indices.