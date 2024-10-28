Here is a JavaScript solution for the problem:

```javascript
const isSorted = (lst) => {
  for (let i = 0; i < lst.length - 1; i++) {
    if (lst[i] >= lst[i + 1]) {
      for (let j = 0; j < i; j++) {
        if (lst[j] === lst[i]) {
          return false;
        }
      }
    } else {
      return false;
    }
  }
  return true;
};
```

This function iterates over the list, checking if each element is less than or equal to the next one. If it finds a pair of elements that don't meet this condition, it immediately returns `false`. If it finishes the loop without finding such a pair, it returns `true`. 

Inside the loop, it also checks if there are any duplicates of the current element. If it finds a duplicate, it returns `false` because the list is not sorted. 

Note that this function assumes that the list only contains integers and does not contain negative numbers. If the list can contain negative numbers or non-integer values, the function would need to be modified accordingly. 