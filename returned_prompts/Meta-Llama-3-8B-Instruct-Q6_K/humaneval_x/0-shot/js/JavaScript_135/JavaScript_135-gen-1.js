```
function canArrange(arr) {
  let maxIndex = -1;
  for (let i = 1; i < arr.length; i++) {
    if (arr[i] <= arr[i - 1]) {
      maxIndex = i;
    }
  }
  return maxIndex;
}

console.log(canArrange([1,2,4,3,5])); // 3
console.log(canArrange([1,2,3])); // -1
```





This JavaScript function `canArrange` iterates through the array from the second element to the end, checking if each element is less than or equal to the previous element. If it finds such an element, it updates the `maxIndex` variable with the current index. If no such element is found, `maxIndex` remains -1. Finally, the function returns the `maxIndex`. If the array does not contain duplicate values, this function correctly returns the largest index of an element which is not greater than or equal to the element immediately preceding it. If no such element exists, it returns -1.