To solve this problem, we'll first iterate through the first `k` elements of the array `arr`. For each element, we'll check if it has at most two digits. If it does, we'll add it to a running total. Finally, we'll return the total sum.

Here's how we can implement this in JavaScript:

```javascript
const addElements = (arr, k) => {
  let sum = 0;

  for (let i = 0; i < k; i++) {
    if (arr[i].toString().length <= 2) {
      sum += arr[i];
    }
  }

  return sum;
};
```

Let's test the function with the provided example:

```javascript
const arr = [111,21,3,4000,5,6,7,8,9];
const k = 4;
console.log(addElements(arr, k));  // Output: 24
```

The function correctly returns 24, which is the sum of 21 and 3 (the first two elements of `arr` that have at most two digits).