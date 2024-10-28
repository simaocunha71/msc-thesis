Here is the solution using JavaScript:

```javascript
const moveOneBall = (arr) => {
    if(arr.length === 0) return true;

    for(let i = 0; i < arr.length; i++) {
        let sorted = true;
        for(let j = 1; j < arr.length; j++) {
            if(arr[j - 1] > arr[j]) {
                sorted = false;
                break;
            }
        }
        if(sorted) return true;
        arr = arr.slice(1).concat([arr[0]]);
    }
    return false;
};
```

In this code, we first check if the array is empty. If it is, we return true because an empty array is considered sorted. 

Then we loop through the array and for each iteration, we check if the array is sorted. We do this by comparing each element with the previous one. If we find a pair of elements where the first one is greater than the second, we set `sorted` to false and break out of the inner loop. 

If the array is not sorted, we perform a right shift operation by slicing the array from the second element to the end and concatenating the first element at the beginning. We then repeat the process with the new array.

If we go through the entire array and find that it is always sorted after a right shift operation, we return true. If we go through the entire array and never find a sorted array, we return false. 

This solution has a time complexity of O(n^2) because we are using two nested loops to check if the array is sorted. The space complexity is O(1) because we are not using any extra space that scales with the input size. 