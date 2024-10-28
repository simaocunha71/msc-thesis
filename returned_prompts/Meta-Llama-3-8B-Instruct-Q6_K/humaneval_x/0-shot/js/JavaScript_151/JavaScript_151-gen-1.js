Here is the solution:
```
const doubleTheDifference = (lst) => {
  let sum = 0;
  for (let num of lst) {
    if (typeof num === 'number' && num % 1 === 0 && num >= 0) {
      if (num % 2 !== 0) {
        sum += num ** 2;
      }
    }
  }
  return sum;
};
```
Explanation:
* We initialize a variable `sum` to store the sum of squares of odd numbers.
* We iterate over the input list using a `for...of` loop.
* For each number, we check if it's a number (using `typeof num === 'number'`), an integer (using `num % 1 === 0`), and non-negative (using `num >= 0`).
* If the number passes these checks, we check if it's odd (using `num % 2 !== 0`).
* If the number is odd, we add its square to the `sum`.
* Finally, we return the `sum`.

Test cases:
```
console.log(doubleTheDifference([1, 3, 2, 0])); // 10
console.log(doubleTheDifference([-1, -2, 0])); // 0
console.log(doubleTheDifference([9, -2])); // 81
console.log(doubleTheDifference([0])); // 0
console.log(doubleTheDifference([])); // 0
```  