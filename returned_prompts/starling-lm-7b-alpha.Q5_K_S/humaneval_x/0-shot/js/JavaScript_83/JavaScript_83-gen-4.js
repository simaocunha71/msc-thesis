
Let's reason about the problem.

The number of positive integers of n digits is 10^n. This is because each digit can be a 0 or a 1-9 and there are n digits. So there are 10 choices for each digit.

Now let's count the number of positive integers of n digits that don't start with 1. There are 9 choices for the first digit. Then there are 10 choices for each of the remaining n-1 digits. So the number of positive integers of n digits that don't start with 1 is 9 * 10^(n-1).

Similarly, the number of positive integers of n digits that don't end with 1 is 10 * 10^(n-1).

So the number of positive integers of n digits that start or end with 1 is 10^n - 9 * 10^(n-1) - 10 * 10^(n-1) = 10^n - 19 * 10^(n-1).

The time complexity of this approach is O(1) since all the operations are constant time.

The space complexity is O(1) as well since no extra memory is used.

Here is the JavaScript implementation:

```javascript
function startsOneEnds(n) {
    return Math.pow(10, n) - 19 * Math.pow(10, n - 1);
}
```

The above implementation first calculates 10^n and 10^(n-1) and then subtracts 19 * 10^(n-1) from 10^n. This gives the correct result in O(1) time and space.

For example, if n = 3, then the number of positive integers of 3 digits that start or end with 1 is 1000 - 190 = 810.

The above implementation will return this result.

The time complexity of this approach is O(1) since all the operations are constant time.

The space complexity is O(1) as well since no extra memory is