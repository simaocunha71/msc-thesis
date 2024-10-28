Here is the JavaScript function that solves the problem:

```javascript
const canArrange = (arr) => {
    for(let i = 0; i < arr.length; i++) {
        if(i > 0 && arr[i] <= arr[i-1]) {
            return i - 1;
        }
    }
    return -1;
};
```
The function iterates through the array and checks each element with the previous one. If the current element is less than or equal to the previous one, it returns the index of the previous element. If no such element is found, it returns -1. This function assumes that the array does not contain duplicate values. 

This function has a time complexity of O(n), where n is the length of the array, and a space complexity of O(1), as it only uses a constant amount of space. 

For example, `canArrange([1,2,4,3,5])` will return `3`, because `3` is the largest index of an element which is not greater than or equal to the element immediately preceding it. Similarly, `canArrange([1,2,3])` will return `-1`, because no such element exists in the array. 