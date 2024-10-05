You can use the `every` method to check if all elements in the list `l` are below the threshold `t`. Here's how you can do it:

```javascript
const belowThreshold = (l, t) => l.every(x => x < t);
```

This will return `true` if all elements in the list `l` are less than the threshold `t`, and `false` otherwise. 

For example, `belowThreshold([1, 2, 4, 10], 100)` will return `true`, and `belowThreshold([1, 20, 4, 10], 5)` will return `false`. 

The `every` method returns `true` if all elements in the list pass the test implemented by the provided function. In this case, the function is `x => x < t`, which checks if an element `x` is less than the threshold `t`. If any element is not less than the threshold, the method will return `false`. If all elements are less than the threshold, the method will return `true`. 

This is a concise and efficient way to solve the problem. It has a time complexity of O(n), where n is the length of the list, because it needs to iterate over all elements in the list. It has a space complexity of O(1), because it only uses a constant amount of space to store the threshold and the result. 