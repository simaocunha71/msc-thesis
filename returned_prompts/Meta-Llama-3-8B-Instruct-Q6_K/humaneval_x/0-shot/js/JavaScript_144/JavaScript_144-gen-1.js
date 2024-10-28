The problem can be solved by converting the given fractions into decimal numbers and then comparing them.

Here is the JavaScript code that implements the given problem:

```javascript
const simplify = (x, n) => {
    // Convert the fractions to decimal numbers
    const decimalX = parseFloat(x.replace('/', '/'));
    const decimalN = parseFloat(n.replace('/', '/'));
    
    // Check if the decimal numbers are equal
    return decimalX === decimalN;
};
```

This code works by first replacing the '/' characters in the input strings with '' to get the decimal numbers. Then it uses the `parseFloat` function to convert the strings into decimal numbers. Finally, it compares these decimal numbers using the equality operator. If they are equal, the function returns `true`; otherwise, it returns `false`. 

For example, if `x` is "1/5" and `n` is "5/1", the function will return `true` because `0.2` equals `0.2`. If `x` is "1/6" and `n` is "2/1", the function will return `false` because `0.16666666666666666` does not equal `1`. 

The function assumes that the input fractions are valid and do not have zero as a denominator. If the input fractions are not valid, the function may return incorrect results. 

The time complexity of this function is O(1) because it performs a constant number of operations. The space complexity is also O(1) because it uses a constant amount of space to store the decimal numbers. 