```
const getPositive = (l) => l.filter(x => x > 0);
```



Explanation:

* The `filter()` method creates a new array with all elements that pass the test implemented by the provided function.
* The function provided to `filter()` is `x => x > 0`, which returns `true` for positive numbers and `false` for non-positive numbers.
* The resulting array only contains positive numbers from the original list.

Test cases:

```
console.log(getPositive([-1, 2, -4, 5, 6])); // [2, 5, 6]
console.log(getPositive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])); // [5, 3, 2, 3, 9, 123, 1]
```



Output:

```
[ 2, 5, 6 ]
[ 5, 3, 2, 3, 9, 123, 1 ]
```



Correctness:

The solution correctly returns only the positive numbers from the input list. It uses the `filter()` method to create a new array with only the elements that pass the test implemented by the provided function. The function `x => x > 0` returns `true` for positive numbers and `false` for non-positive numbers, effectively filtering out the negative numbers. The resulting array only contains positive numbers from the original list.