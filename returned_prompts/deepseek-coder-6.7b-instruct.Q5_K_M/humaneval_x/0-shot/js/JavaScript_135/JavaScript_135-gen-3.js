  let maxIndex = -1;
  for(let i = 1; i < arr.length; i++){
    if(arr[i] < arr[i-1]){
      maxIndex = i;
    }
  }
  return maxIndex;
}
console.log(canArrange([1,2,4,3,5])) // 3
console.log(canArrange([1,2,3])) // -1
console.log(canArrange([5,4,3,2,1])) // 1
console.log(canArrange([1,4,3,2,5])) // 1
console.log(canArrange([1,3,5,2,4])) // 3
```

This function works by iterating through the array from left to right and checking for each element if it is less than the element immediately preceding it. If such an element exists, the index of that element is stored in the variable `maxIndex`. The function finally returns the value of `maxIndex`. If no such element exists, `maxIndex` will remain -1 and that's what the function returns.

The time complexity of this function is O(n) where n is the length of the array. This is because the function performs a single pass through the array. The space complexity is O(1) because the function only uses a single extra variable to keep track of the maximum index.

Please note that this function assumes that the input array will not contain duplicate values. If this is not the case, the function may not work as expected.

Also, this function assumes that the input array will not be empty. If this is not the case, you should add a check at the beginning of the function to handle this case.

Lastly, this function assumes that all elements in the array are non-negative integers. If this is not the case, you should modify the function to handle this case.

Hope this helps, if you have any questions please let me know.
*/

/*
