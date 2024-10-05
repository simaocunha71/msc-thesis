```javascript
function greatestCommonDivisor(a, b) {
    if (b === 0) {
        return a;
    }
    return greatestCommonDivisor(b, a % b);
}
```
Explanation:

*   We use a recursive approach to find the greatest common divisor (GCD) of two integers `a` and `b`.
*   The base case is when `b` is 0, in which case the GCD is `a`.
*   Otherwise, we recursively call the function with `b` and the remainder of `a` divided by `b` (i.e., `a % b`).
*   This process continues until `b` is 0, at which point the GCD is returned.

Example usage:
```javascript
console.log(greatestCommonDivisor(3, 5)); // Output: 1
console.log(greatestCommonDivisor(25, 15)); // Output: 5
```