To solve this kata, first we need to filter out all the numbers that don't have any even digit. We can achieve this by using the `filter()` function in JavaScript along with a regular expression.

The regular expression `/[2468]/` matches any digit that is even. We can use this regular expression in a positive lookahead to ensure that the entire number doesn't have any even digits. Here's an example of how to write the regular expression:

```
/^(?!.*[2468])/
```

This regular expression matches any string that doesn't contain any even digits. It uses the `^` anchor to match the beginning of the string and the `.*` part to match any characters (except newline) zero or more times. The `[2468]` part matches any even digit, and the `(?!...)` part is a positive lookahead that asserts that the even digit is not present in the string.

To filter out all the numbers that don't have any even digits, we can use the `filter()` function along with this regular expression. The `filter()` function will return a new array with all the elements that pass the test, which in this case means all the numbers that don't have any even digits.

Next, we need to sort the resulting array in increasing order. We can achieve this by using the `sort()` function along with a comparison function. The comparison function should return a negative value if the first element is less than the second element, a positive value if the first element is greater than the second element, and zero if the elements are equal.

Here's an example of how to write the comparison function:

```
(a, b) => a - b
```

This function subtracts `b` from `a`, so if `a` is less than `b`, it returns a negative value, if `a` is greater than `b`, it returns a positive value, and if `a` is equal to `b`, it returns zero. The `sort()` function will use this comparison function to sort the array in increasing order.

Finally, we can combine all the steps together to write the `uniqueDigits` function:

```javascript
const uniqueDigits = (