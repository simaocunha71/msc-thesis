```
const maximum = (arr, k) => {
  return arr.sort((a, b) => b - a).slice(0, k);
};
```
Explanation:

* The `slice(0, k)` method is used to get the first `k` elements of the sorted array, which are the maximum `k` numbers in the original array.
* The `sort((a, b) => b - a)` method is used to sort the array in descending order, so the maximum numbers come first.
* The `sort()` method returns a new array, so we don't need to worry about modifying the original array.