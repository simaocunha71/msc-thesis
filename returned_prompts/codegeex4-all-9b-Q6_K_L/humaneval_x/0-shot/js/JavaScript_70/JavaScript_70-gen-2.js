You can solve this problem by using the following steps:

1. Create two empty arrays, `min` and `max`, to store the minimum and maximum values of the list.
2. Sort the list in ascending order.
3. Iterate through the sorted list and for each element:
    - If the current index is even, add the element to the `min` array.
    - If the current index is odd, add the element to the `max` array.
4. Concatenate the `min` and `max` arrays in reverse order.
5. Return the concatenated array.

Here is the implementation of the `strangeSortList` function in JavaScript:

```javascript
const strangeSortList = (lst) => {
  const min = [];
  const max = [];
  const sorted = lst.slice().sort((a, b) => a - b);

  for (let i = 0; i < sorted.length; i++) {
    if (i % 2 === 0) {
      min.push(sorted[i]);
    } else {
      max.push(sorted[i]);
    }
  }

  return [...max.reverse(), ...min.reverse()];
};
```

The `strangeSortList` function takes an array of integers `lst` as input and returns a new array that is sorted according to the strange sorting rule. The function first creates two empty arrays, `min` and `max`, to store the minimum and maximum values of the list. Then, it creates a copy of the input list and sorts it in ascending order using the `sort` method. Next, it iterates through the sorted list and for each element, it checks if the current index is even or odd. If the index is even, it adds the element to the `min` array. If the index is odd, it adds the element to the `max` array. Finally, it concatenates the `max` and `min` arrays in reverse order and returns the concatenated array.