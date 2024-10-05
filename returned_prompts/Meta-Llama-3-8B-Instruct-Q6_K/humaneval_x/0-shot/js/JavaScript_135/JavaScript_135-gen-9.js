Here is the JavaScript function to solve the problem:

```javascript
const canArrange = (arr) => {
  let largestIndex = -1;
  for (let i = 1; i < arr.length; i++) {
    if (arr[i] <= arr[i - 1]) {
      largestIndex = i;
    }
  }
  return largestIndex;
};
```

Explanation:
The function iterates over the array from the second element to the end. For each element, it checks if the current element is less than or equal to the previous element. If it is, it updates the largestIndex to the current index. After iterating over the entire array, it returns the largestIndex. If no such element is found, the function returns -1. This solution assumes that the array contains unique elements, as per the problem statement. If the array can contain duplicate values, additional logic would be needed to handle this case.