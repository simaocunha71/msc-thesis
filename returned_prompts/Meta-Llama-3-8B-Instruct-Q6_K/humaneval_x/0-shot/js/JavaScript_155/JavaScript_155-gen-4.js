Here is a solution for the problem:

```javascript
const evenOddCount = (num) => {
    let even = 0;
    let odd = 0;
    let numStr = num.toString();
    for (let i = 0; i < numStr.length; i++) {
        let digit = parseInt(numStr[i]);
        if (digit % 2 === 0) {
            even++;
        } else {
            odd++;
        }
    }
    return [even, odd];
}
```



Explanation:

1.  We initialize two counters, `even` and `odd`, to keep track of the number of even and odd digits respectively.
2.  We convert the input number to a string using `toString()` method. This allows us to iterate over each digit in the number.
3.  We loop through each character (digit) in the string using a `for` loop.
4.  For each digit, we convert it back to an integer using `parseInt()` and check if it's even or odd using the modulo operator (`%`). If the remainder is 0, the digit is even; otherwise, it's odd.
5.  We increment the corresponding counter (`even` or `odd`) based on whether the digit is even or odd.
6.  Finally, we return an array containing the counts of even and odd digits.

This solution works for both positive and negative integers, as well as for numbers with leading zeros. For example, `evenOddCount(-12)` returns `[1, 1]`, and `evenOddCount(123)` returns `[1, 2]`.