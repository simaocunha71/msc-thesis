Here is the solution in JavaScript:

```javascript
const add = (lst) => {
  let sum = 0;
  for(let i = 0; i < lst.length; i++) {
    if(lst[i] % 2 === 0 && i % 2 !== 0) {
      sum += lst[i];
    }
  }
  return sum;
}
```

The function `add` takes in an array of integers `lst` as its argument. It initializes a variable `sum` to 0, which will be used to store the sum of the even elements at odd indices.

The function then loops through the array using a `for` loop. Inside the loop, it checks if the current element `lst[i]` is even (`lst[i] % 2 === 0`) and its index `i` is odd (`i % 2 !== 0`). If both conditions are true, it adds the current element to `sum`.

Finally, the function returns the value of `sum`, which is the sum of the even elements at odd indices.