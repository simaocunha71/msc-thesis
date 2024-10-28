Here is a JavaScript function that solves the problem:

```javascript
const canArrange = (arr) => {
    let maxIndex = -1;
    for(let i = 1; i < arr.length; i++) {
        if(arr[i] <= arr[i-1]) {
            maxIndex = i;
        }
    }
    return maxIndex;
}
```

This function iterates through the array, starting from the second element. If it finds an element that is not greater than or equal to the previous element, it updates the maxIndex variable. If no such element is found, the function returns -1.

The time complexity of this function is O(n), where n is the length of the array, because it iterates through the array once. The space complexity is O(1), because it uses a constant amount of space to store the maxIndex variable.