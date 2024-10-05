Here is a solution using JavaScript:
```
const canArrange = (arr) => {
  let maxIndex = -1;
  for (let i = 1; i < arr.length; i++) {
    if (arr[i] <= arr[i - 1]) {
      maxIndex = i;
    }
  }
  return maxIndex;
};
```
Explanation:

* We initialize `maxIndex` to -1, which will be returned if no such element is found.
* We iterate through the array starting from the second element (index 1) to the end.
* For each element, we check if it is less than or equal to the previous element. If it is, we update `maxIndex` with the current index.
* Finally, we return `maxIndex`.

Testing:
```
console.log(canArrange([1, 2, 4, 3, 5])); // 3
console.log(canArrange([1, 2, 3])); // -1
```
This solution has a time complexity of O(n), where n is the length of the input array, as we only iterate through the array once. The space complexity is O(1), as we only use a constant amount of space to store the `maxIndex` variable.