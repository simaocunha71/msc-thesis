```
const moveOneBall = (arr) => {
    if (arr.length === 0) return true;
    let count = 0;
    for (let i = 1; i < arr.length; i++) {
        if (arr[i] >= arr[i - 1]) continue;
        count++;
    }
    return count <= 1;
};
```
Explanation:
The algorithm works by iterating through the array and keeping track of the number of times a right shift operation is needed to make the array non-decreasing. If the array is already sorted or only one element needs to be shifted to the right to make it non-decreasing, then the function returns true. Otherwise, it returns false.

In the given array, if the current element is greater than or equal to the previous element, it means that the array is already non-decreasing, so we can skip this element and move on to the next one. If the current element is less than the previous element, it means that a right shift operation is needed to make the array non-decreasing, so we increment the count variable.

Finally, we return whether the count is less than or equal to 1. If it is, it means that we can make the array non-decreasing by performing at most one right shift operation, so we return true. Otherwise, we return false.