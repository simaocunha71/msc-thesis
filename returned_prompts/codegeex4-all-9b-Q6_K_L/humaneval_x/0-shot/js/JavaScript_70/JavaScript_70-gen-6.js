The function strangeSortList takes a list of integers lst as input and returns a new list that is sorted in a strange order. The order is such that the minimum value of the list is followed by the maximum value of the remaining integers, then the second minimum value, and so on.

Here's the step-by-step explanation of the code:

1. Initialize an empty list result to store the sorted values.
2. Create a copy of the input list lst to avoid mutating the original list.
3. While the copied list is not empty:
   - Find the index of the minimum value in the copied list using the indexOf method.
   - Add the minimum value to the result list.
   - Remove the minimum value from the copied list using the splice method.
   - Find the index of the maximum value in the copied list using the indexOf method.
   - Add the maximum value to the result list.
   - Remove the maximum value from the copied list using the splice method.
4. Return the result list.

Here's the complete code:

```javascript
const strangeSortList = (lst) => {
  let result = [];
  let copy = [...lst];
  while (copy.length > 0) {
    let minIndex = copy.indexOf(Math.min(...copy));
    result.push(copy[minIndex]);
    copy.splice(minIndex, 1);
    if (copy.length > 0) {
      let maxIndex = copy.indexOf(Math.max(...copy));
      result.push(copy[maxIndex]);
      copy.splice(maxIndex, 1);
    }
  }
  return result;
};
```

The time complexity of this function is O(n^2), where n is the length of the input list lst. This is because for each element in the list, we find the minimum and maximum values using nested loops.