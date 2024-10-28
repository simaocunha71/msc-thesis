Here is the JavaScript solution for the problem:

```javascript
const canArrange = (arr) => {
    let maxIndex = -1;
    for(let i = 0; i < arr.length; i++) {
        if(i > 0 && arr[i] <= arr[i - 1]) {
            maxIndex = i;
        }
    }
    return maxIndex;
};
```

Explanation: 
This function iterates through the array and checks if the current element is less than or equal to the previous element. If it finds such an element, it updates the maxIndex variable with the current index. Finally, it returns the maxIndex. If no such element is found, the function returns -1. 

For example, in the array [1,2,4,3,5], the function will return 3 because the element at index 3 (3) is not greater than or equal to the element at index 2 (4). In the array [1,2,3], the function will return -1 because there is no such element. 

Note: The given array will not contain duplicate values. This is mentioned in the problem statement. Therefore, we don't need to worry about duplicate values while solving this problem. 