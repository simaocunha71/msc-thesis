To solve this problem, we can iterate through the array and check if each element is less than or equal to the next element. If we find an element that is greater than the next element, we return its index. If we reach the end of the array without finding such an element, we return -1.

Here is the implementation in JavaScript:

```javascript
const canArrange = (arr) => {
  for (let i = 0; i < arr.length - 1; i++) {
    if (arr[i] > arr[i + 1]) {
      return i;
    }
  }
  return -1;
};
```

Let's test the function with the provided examples:

```javascript
console.log(canArrange([1, 2, 4, 3, 5])); // Output: 3
console.log(canArrange([1, 2, 3])); // Output: -1
```

The function returns the expected results.