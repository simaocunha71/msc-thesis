```javascript
const add = (lst) => {
  let sum = 0;
  for (let i = 1; i < lst.length; i += 2) {
    if (lst[i] % 2 === 0) {
      sum += lst[i];
    }
  }
  return sum;
};
```
Explanation:
The function `add` takes a list of integers `lst` as an argument. It initializes a variable `sum` to 0, which will be used to store the sum of the even elements at odd indices.

The function then uses a for loop to iterate over the list, starting from the second element (index 1) and incrementing by 2 each time. This ensures that we only consider the elements at odd indices.

Inside the loop, we check if the current element is even by using the modulo operator (`%`). If it is, we add it to the `sum`.

Finally, the function returns the `sum`.

For example, if we call `add([4, 2, 6, 7])`, the function will iterate over the list as follows:

* `i = 1`, `lst[i] = 2`, `sum = 0 + 2 = 2`
* `i = 3`, `lst[i] = 6`, `sum = 2 + 6 = 8`
* `i = 5` (skipped, since `i` is incremented by 2)

The function returns `8`, which is the sum of the even elements at odd indices.