We can use a filter method to get the even elements at odd indices and then use reduce method to sum them up. Here is the code:

```javascript
const add = (lst) => {
  return lst.filter((x, i) => i % 2 !== 0 && x % 2 === 0).reduce((acc, curr) => acc + curr, 0);
}
```

Explanation:

1. `filter((x, i) => i % 2 !== 0 && x % 2 === 0)`: This will filter the array to include only the elements that are at odd indices (`i % 2 !== 0`) and are even (`x % 2 === 0`).

2. `reduce((acc, curr) => acc + curr, 0)`: This will sum up all the even elements at odd indices. The initial value of the accumulator (`acc`) is set to 0. For each element in the array, the accumulator is updated by adding the current element (`curr`). The final sum is returned.

For example, if the input is `[4, 2, 6, 7]`, the output will be `2` because `2` is the only even element at an odd index. If the input is `[1, 3, 5, 2, 7]`, the output will be `2` because `2` is the only even element at an odd index. .


This code works for any length of list and any numbers in the list. It's also case-insensitive because JavaScript is a case-insensitive language. .


The time complexity of this code is O(n), where n is the length of the list, because we're doing a constant amount of work for each element in the list. The space complexity is also O(n) because in the worst case, the filter method could return a list of the same length as the original list. .


This code assumes that the input is a non-empty list of integers. If the input could be an empty list or a list with non-integer elements, you would need to add error checking code to handle these cases. .


I hope this helps! Let me know if you have any questions.