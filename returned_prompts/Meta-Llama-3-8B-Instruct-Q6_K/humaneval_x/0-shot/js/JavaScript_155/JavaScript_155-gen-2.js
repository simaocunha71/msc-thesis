Here is a JavaScript solution for the problem:

```javascript
const evenOddCount = (num) => {
    let evenCount = 0;
    let oddCount = 0;
    let numStr = String(Math.abs(num)); // convert to string and remove negative sign

    for (let i = 0; i < numStr.length; i++) {
        let digit = parseInt(numStr[i]);
        if (digit % 2 === 0) {
            evenCount++;
        } else {
            oddCount++;
        }
    }
    return [evenCount, oddCount];
};
```
In this solution, we first convert the input number to a string and remove the negative sign (if the number is negative). Then we iterate over each character (digit) in the string. If the digit is even, we increment the `evenCount`, otherwise we increment the `oddCount`. Finally, we return an array with the counts of even and odd digits.

For example, if the input is `-12`, we convert it to a string `"12"` and remove the negative sign. Then we iterate over the digits, `1` and `2`. `1` is odd, so we increment `oddCount` to `1`, and `2` is even, so we increment `evenCount` to `1`. The output is `[1, 1]`.

If the input is `123`, we convert it to a string `"123"` and iterate over the digits, `1`, `2`, and `3`. `1` is odd, so we increment `oddCount` to `1`, `2` is even, so we increment `evenCount` to `1`, and `3` is odd, so we increment `oddCount` to `2`. The output is `[1, 2]`.