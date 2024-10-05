```
const sortThird = (l) => {
  return l.map((val, index) => index % 3 !== 0 ? val : [...l.slice(index, index + 3)].sort((a, b) => a - b)[0]);
};
```
This function works by mapping over the input list `l`. For each element at index `i`, it checks if `i` is not divisible by 3 (`index % 3 !== 0`). If it's not, it just returns the original value. If it is, it extracts the three elements starting at index `i` (`l.slice(index, index + 3)`), sorts them (`sort((a, b) => a - b)`), and returns the first element of the sorted list (`[0]`). The resulting list is then returned. This way, the list is modified to have the values at the indices divisible by 3 sorted.