```javascript
function monotonic(l) {
    return (l.every((x, i, a) => i === 0 || x >= a[i - 1]) ||
            l.every((x, i, a) => i === 0 || x <= a[i - 1]));
}
```
Explanation:
The function `monotonic` checks if the list `l` is monotonically increasing or decreasing. It does this by checking if every element is greater than or equal to the previous element, or if every element is less than or equal to the previous element. The `every` method is used to check if every element in the list satisfies the condition. If every element is greater than or equal to the previous element, the list is monotonically increasing. If every element is less than or equal to the previous element, the list is monotonically decreasing. The function returns `true` if the list is monotonically increasing or decreasing, and `false` otherwise. 

The `every` method returns `true` if every element in the list satisfies the condition, and `false` otherwise. The condition is specified using an arrow function that takes three arguments: the current element `x`, the current index `i`, and the array `a`. The condition checks if the current element is greater than or equal to the previous element (`x >= a[i - 1]`) or less than or equal to the previous element (`x <= a[i - 1]`).

In the example, the list `[1, 2, 4, 20]` is monotonically increasing because every element is greater than or equal to the previous element. The list `[1, 20, 4, 10]` is not monotonically increasing because the element `20` is greater than the previous element, but the element `4` is less than the previous element. The list `[4, 1, 0, -10]` is monotonically decreasing because every element is less than or equal to the previous element. 

The function `monotonic` returns `true` for the first and third lists, and `false` for the second list. 

Here is the code:

```javascript
function monotonic(l) {
    return (l.every((x, i, a) => i === 0 || x >= a[i - 1]) ||
            l.every((x, i, a) => i === 0 || x <= a