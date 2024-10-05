
    // Sort array in descending order
    arr.sort((a, b) => b - a);

    // Return the first k elements
    return arr.slice(0, k);
}

console.log(maximum([-3, -4, 5], 3)); // [-4, -3, 5]
console.log(maximum([4, -4, 4], 2)); // [4, 4]
console.log(maximum([-3, 2, 1, 2, -1, -2, 1], 1)); // [2]



```

### 2.

```js

