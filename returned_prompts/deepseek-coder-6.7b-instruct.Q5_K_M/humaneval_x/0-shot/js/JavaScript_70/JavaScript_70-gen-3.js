  lst.sort((a, b) => a - b);
  let result = [];

  while (lst.length) {
    result.push(lst.shift());
    if (lst.length) {
      result.push(lst.pop());
    }
  }

  return result;
}

console.log(strangeSortList([1, 2, 3, 4])); // [1, 4, 2, 3]
console.log(strangeSortList([5, 5, 5, 5])); // [5, 5, 5, 5]
console.log(strangeSortList([])); // []

```


## Answer

This problem can be solved by using Javascript's built-in sort function and looping through the array from both ends.

In Javascript, the sort function sorts elements of an array by converting them to strings and comparing their sequences of UTF-16 code unit values. We can provide our own sorting function to sort the numbers in ascending order.

In the while loop, we remove the smallest and largest number from the sorted array and add them to the result array. This process continues until the array is empty.

```javascript
const strangeSortList = (lst) => {
  lst.sort((a, b) => a - b);
  let result = [];

  while (lst.length) {
    result.push(lst.shift());
    if (lst.length) {
      result.push(lst.pop());
    }
  }

  return result;
}

console.log(strangeSortList([1, 2, 3, 4])); // [1, 4, 2, 3]
console.log(strangeSortList([5, 5, 5, 5])); // [5, 5, 5, 5]
console.log(strangeSortList([])); // []
```

This function will return the input array sorted in a strange order as described in the problem statement.

Note: This solution assumes that the input array will not contain non-integer or non-numeric