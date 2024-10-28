```javascript
const moveOneBall = (arr) => {
  if (arr.length === 0) return true;
  let maxIndex = 0;
  for (let i = 1; i < arr.length; i++) {
    if (arr[i] > arr[maxIndex]) {
      maxIndex = i;
    }
  }
  for (let i = 0; i < arr.length; i++) {
    if (arr[i] > arr[(i + maxIndex) % arr.length]) {
      return false;
    }
  }
  return true;
};
```


Explanation:
This function checks if the given array can be sorted in non-decreasing order by performing right shift operations. 

First, it checks if the array is empty. If it is, it returns true because an empty array is already sorted.

Then, it finds the maximum element in the array and its index.

After that, it checks if the maximum element is in its correct position. If not, it returns false because the array cannot be sorted in non-decreasing order.

If the maximum element is in its correct position, it checks if the array can be sorted by performing right shift operations. It does this by iterating over the array and checking if each element is less than or equal to the element at the index calculated by adding the current index and the maximum index modulo the length of the array. If it finds an element that is greater than the element at the calculated index, it returns false.

If the function does not find any elements that are greater than the elements at the calculated indices, it returns true, indicating that the array can be sorted in non-decreasing order by performing right shift operations.