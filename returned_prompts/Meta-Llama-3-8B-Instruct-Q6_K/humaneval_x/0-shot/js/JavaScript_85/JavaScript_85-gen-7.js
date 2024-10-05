Here is a JavaScript solution for the problem:

```javascript
const add = (lst) => {
  let sum = 0;
  for (let i = 0; i < lst.length; i++) {
    if (i % 2 !== 0 && lst[i] % 2 === 0) {
      sum += lst[i];
    }
  }
  return sum;
};

console.log(add([4, 2, 6, 7])); // Output: 2
```

In this solution, we use a for loop to iterate over the elements of the list. We check if the index `i` is odd (`i % 2 !== 0`) and if the element at that index is even (`lst[i] % 2 === 0`). If both conditions are true, we add the element to the sum. Finally, we return the sum.