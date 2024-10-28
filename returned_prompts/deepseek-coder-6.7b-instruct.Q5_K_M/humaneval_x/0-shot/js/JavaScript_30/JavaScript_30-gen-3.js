  return l.filter(n => n > 0);
}

console.log(getPositive([-1, 2, 4, 5, 6]));
console.log(getPositive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]));


A: Here is the JavaScript code to solve this problem.

```javascript
const getPositive = (arr) => {
  return arr.filter(num => num > 0);
}

console.log(getPositive([-1, 2, -4, 5, 6])); // Output: [2, 5, 6]
console.log(getPositive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])); // Output: [5, 3, 2, 3, 9, 123, 1]
```

In the `getPositive` function, we use the `filter` function to create a new array that includes only the positive numbers from the original array. We use a ternary operator to check if each number is greater than 0. If it is, we include it in the new array.

The `filter` function creates a new array with all elements that pass the test implemented by the provided function. In this case, the test is whether each number is greater than 0.

Finally, we print the results of calling `getPositive` with an array of numbers.

I hope this helps you understand how this works.

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

