Here is the solution:

```javascript
const sortEven = (l) => {
  return l.map((val, index) => {
    if (index % 2 === 0) {
      return l.slice(0, index).filter((x) => x % 2 === 0).sort((a, b) => a - b)[0];
    } else {
      return val;
    }
  });
};
```

Explanation:
The function uses the `map` method to iterate over the input list `l`. For each element `val` at index `index`, it checks if the index is even (`index % 2 === 0`). If it is, it returns the smallest even element in the list (up to that index) by using `filter` to get all even elements, sorting them, and taking the first element. If the index is odd, it returns the original value. The result is a new list where the even indices have the smallest even elements in the original list.