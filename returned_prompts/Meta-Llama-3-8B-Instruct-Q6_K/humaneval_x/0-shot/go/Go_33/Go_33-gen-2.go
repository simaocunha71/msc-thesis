Here is a JavaScript solution for the problem:

```javascript
const strangeSortList = (lst) => {
  if (lst.length === 0) {
    return [];
  }

  lst.sort((a, b) => {
    if (a < b) {
      return -1;
    } else if (a > b) {
      return 1;
    } else {
      return 0;
    }
  });

  let result = [];
  let min = lst[0];
  let max = lst[0];

  for (let i = 0; i < lst.length; i++) {
    if (lst[i] === min) {
      result.push(min);
      min = getMin(result.concat(lst.slice(i + 1)));
    } else if (lst[i] === max) {
      result.push(max);
      max = getMax(result.concat(lst.slice(i + 1)));
    }
  }

  return result;
};

const getMin = (arr) => {
  let min = arr[0];
  for (let i = 1; i < arr.length; i++) {
    if (arr[i] < min) {
      min = arr[i];
    }
  }
  return min;
};

const getMax = (arr) => {
  let max = arr[0];
  for (let i = 1; i < arr.length; i++) {
    if (arr[i] > max) {
      max = arr[i];
    }
  }
  return max;
};
```

The function `strangeSortList` first sorts the input list in ascending order. Then it iterates over the sorted list and pushes the minimum and maximum values to the result list. The function `getMin` and `getMax` are helper functions used to find the minimum and maximum values in an array respectively. The result list will be in the strange order specified in the problem.  */ 