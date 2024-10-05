The problem asks to add the even elements that are at odd indices in the given list of integers.

Here's a solution in JavaScript:

```javascript
const add = (lst) => {
  let sum = 0;
  for(let i = 1; i < lst.length; i += 2) {
    if(lst[i] % 2 === 0) {
      sum += lst[i];
    }
  }
  return sum;
};
```
This function initializes a variable `sum` to 0 and then iterates over the list using a for loop. It starts from the second element (index 1) and increments the index by 2 in each iteration, effectively considering only the elements at odd indices. If the element at the current index is even (i.e., `lst[i] % 2 === 0`), it adds the element to the `sum`. Finally, the function returns the `sum`.