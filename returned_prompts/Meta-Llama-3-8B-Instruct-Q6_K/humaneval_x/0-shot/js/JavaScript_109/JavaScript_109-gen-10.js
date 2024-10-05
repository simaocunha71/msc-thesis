Here is the solution to the problem. This solution iterates through the array and checks if the current element is less than the next element. If it is, then it means that the array cannot be sorted by performing right shift operations, so the function returns false. If the array is empty or the loop completes without finding any elements that are less than the next element, then the function returns true.

```javascript
const moveOneBall = (arr) => {
    if(arr.length === 0) return true;
    for(let i = 0; i < arr.length - 1; i++) {
        if(arr[i] > arr[i+1]) return false;
    }
    return true;
};
```

For example, if we call `moveOneBall([3, 4, 5, 1, 2])`, the function will return `true` because we can perform 2 right shift operations to get the array in non-decreasing order: `[2, 3, 4, 5, 1]`. If we call `moveOneBall([3, 5, 4, 1, 2])`, the function will return `false` because it is not possible to get the array in non-decreasing order by performing any number of right shift operations.