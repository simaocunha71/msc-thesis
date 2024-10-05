```
const sortThird = (l) => {
  return l.map((x, i) => i % 3 !== 0 ? x : l.slice(0, i).concat(...l.slice(i).sort((a, b) => a - b)));
};
```
This function uses the `map` method to iterate over the input list `l`. For each element `x` at index `i`, it checks if `i` is not divisible by 3 using the modulo operator (`i % 3 !== 0`). If it is not, it returns the original element `x`. If it is, it returns a new list created by concatenating the elements before the current index (`l.slice(0, i)`) with the sorted elements after the current index (`l.slice(i).sort((a, b) => a - b)`). The `slice` method is used to create new lists from the original list, and the `sort` method is used to sort the elements in ascending order. The `concat` method is used to concatenate the two lists. The resulting list is then returned.