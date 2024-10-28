Here is the solution in JavaScript:

```javascript
const addElements = (arr, k) => {
    let sum = 0;
    for (let i = 0; i < k; i++) {
        if (String(arr[i]).length <= 2) {
            sum += arr[i];
        }
    }
    return sum;
};
```

Explanation:

1. Initialize a variable `sum` to 0 to keep track of the sum of the elements with at most two digits.
2. Loop through the first `k` elements of the array `arr`.
3. For each element, convert it to a string and check its length using the `length` property. If the length is less than or equal to 2, it means the element has at most two digits.
4. If the element has at most two digits, add it to the `sum`.
5. After the loop, return the `sum`.

This solution has a time complexity of O(k) because we are iterating through the first `k` elements of the array. The space complexity is O(1) because we are using a constant amount of space to store the `sum`.