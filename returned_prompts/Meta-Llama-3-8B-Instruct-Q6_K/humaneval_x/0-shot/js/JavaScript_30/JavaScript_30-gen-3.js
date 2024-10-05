```
const getPositive = (l) => l.filter(x => x > 0);
```


Explanation:

The `filter()` method creates a new array with all elements that pass the test implemented by the provided function. In this case, the function is `x => x > 0`, which returns `true` if the element is greater than 0 and `false` otherwise.

So, when you call `getPositive([-1, 2, -4, 5, 6])`, it will return `l.filter(x => x > 0)`, which is equivalent to `[2, 5, 6]`. The same applies to the second example.

You can test it with the following code:

```javascript
console.log(getPositive([-1, 2, -4, 5, 6])); // Output: [2, 5, 6]
console.log(getPositive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])); // Output: [5, 3, 2, 3, 9, 123, 1]
```


Hope this helps! Let me know if you have any further questions.