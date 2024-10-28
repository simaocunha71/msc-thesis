You can solve this problem using a list comprehension. Here is the solution:
```
const getPositive = (l) => l.filter(x => x > 0)
```
Explanation:

* `filter()` is a method that creates a new list with all elements that pass the test implemented by the provided function.
* `x => x > 0` is an anonymous function that takes an element `x` and returns `true` if `x` is greater than 0, and `false` otherwise.

Example usage:
```
console.log(getPositive([-1, 2, -4, 5, 6])); // Output: [2, 5, 6]
console.log(getPositive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])); // Output: [5, 3, 2, 3, 9, 123, 1]
```
This solution is concise and efficient, as it uses the built-in `filter()` method to achieve the desired result. It also works with lists of any size, not just small lists.