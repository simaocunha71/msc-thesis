```javascript
const sortEven = (l) => {
  const result = [];
  for (let i = 0; i < l.length; i++) {
    if (i % 2 === 0) {
      result.push(l[i]);
    } else {
      result.push(...l.slice(0, i).filter((x, index) => index % 2 === 0).sort((a, b) => a - b));
    }
  }
  return result;
};
```


Explanation:
This function iterates over the input list `l` and constructs a new list `result`. It uses the modulo operator `%` to check if the current index `i` is even or odd. If `i` is even, it simply appends the corresponding element from `l` to `result`. If `i` is odd, it appends a sorted version of the even-indexed elements from `l` that come before `i` in the original list. The `filter` method is used to select only the even-indexed elements, and the `sort` method is used to sort them in ascending order. The spread operator `...` is used to flatten the sorted array into a single element. Finally, the function returns the constructed list `result`.