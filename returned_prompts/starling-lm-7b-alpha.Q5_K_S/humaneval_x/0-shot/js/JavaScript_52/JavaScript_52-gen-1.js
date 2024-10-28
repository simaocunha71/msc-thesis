To solve this problem, you can use the `every` method from JavaScript array. The `every` method tests whether all elements in the array pass the test implemented by the provided function. If all the elements pass the test, the method returns true. Otherwise, it returns false.

Here is the step-by-step solution:

1. Define the function `belowThreshold` that takes two parameters: `l` (the array of numbers) and `t` (the threshold).

2. Use the `every` method on the array `l` with a callback function that checks if each element of the array is less than the threshold `t`. The callback function should return `true` if the condition is met and `false` otherwise.

3. The `every` method will return `true` if all the elements in the array pass the test (i.e., if all the numbers in `l` are below the threshold `t`), and `false` otherwise.

4. Return the result of the `every` method as the result of the `belowThreshold` function.

Here's the code implementation of the solution:

```javascript
const belowThreshold = (l, t) => {
  return l.every(num => num < t);
};
```

You can now use the `belowThreshold` function to check if all the numbers in a list are below a given threshold. For example:

```javascript
console.log(belowThreshold([1, 2, 4, 10], 100));  // Output: true
console.log(belowThreshold([1, 20, 4, 10], 5));   // Output: false
```

In the first example, all the numbers in the list `[1, 2, 4, 10]` are below the threshold `100`, so the function returns `true`. In the second example, the number `20` is not below the threshold `5`, so the function returns `false`.

I hope this helps! Let me know if you have any more questions.

*/

/*
  >>> belowThreshold([1, 2, 4, 10], 100)
  true
  >>> belowThreshold([1, 20,