```
function pluck(arr) {
  let minEven = Infinity;
  let minIndex = -1;
  for (let i = 0; i < arr.length; i++) {
    if (arr[i] % 2 === 0 && arr[i] < minEven) {
      minEven = arr[i];
      minIndex = i;
    }
  }
  return minEven === Infinity ? [] : [minEven, minIndex];
}
```


Explanation:
This problem can be solved by iterating over the array and finding the smallest even value and its index. If no even value is found, the function returns an empty list. The function uses a for loop to iterate over the array and checks each element to see if it's even. If an even value is found and it's smaller than the current minimum, the minimum is updated and its index is saved. Finally, the function returns the minimum even value and its index in a list. If no even value is found, the function returns an empty list. This solution has a time complexity of O(n) where n is the length of the array.