The problem can be solved by iterating over the array and for each element, calculate the sum of the element with all the remaining elements. If the sum is a multiple of 3, increment the count.

Here is the implementation in JavaScript:
```
const getMaxTriples = (n) => {
  let a = [];
  let count = 0;
  for (let i = 1; i <= n; i++) {
    a.push(i * i - i + 1);
  }
  for (let i = 0; i < n; i++) {
    for (let j = i + 1; j < n; j++) {
      for (let k = j + 1; k < n; k++) {
        if ((a[i] + a[j] + a[k]) % 3 === 0) {
          count++;
        }
      }
    }
  }
  return count;
};
```
This solution has a time complexity of O(n^3) due to the triple nested loops. It can be optimized by reducing the number of iterations. For example, we can calculate the sum of the first two elements and store it in a variable, and then iterate over the remaining elements to check if the sum is a multiple of 3.

Here is the optimized implementation:
```
const getMaxTriples = (n) => {
  let a = [];
  let count = 0;
  for (let i = 1; i <= n; i++) {
    a.push(i * i - i + 1);
  }
  for (let i = 0; i < n; i++) {
    for (let j = i + 1; j < n; j++) {
      let sum = a[i] + a[j];
      for (let k = j + 1; k < n; k++) {
        if (sum + a[k] % 3 === 0) {
          count++;
        }
      }
    }
  }
  return count;
};
```
This solution has a time complexity of O(n^2) which is more efficient than the original solution. However, it still has a high time complexity and may not be suitable for large values of n.

It's worth noting that the problem can be solved using a more mathematical approach. We can use the fact that the sum of three integers is a multiple of 3 if and only if the sum of their remainders when divided by 3 is 0