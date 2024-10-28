```javascript
const evenOddCount = (num) => {
    let even = 0, odd = 0;
    num = Math.abs(num).toString();
    for (let i = 0; i < num.length; i++) {
        let digit = parseInt(num[i]);
        if (digit % 2 === 0) even++;
        else odd++;
    }
    return [even, odd];
};
```


Explanation:

- We use `Math.abs(num)` to convert the number to its absolute value, so we can process negative numbers as well.
- We convert the number to a string using `toString()` to easily iterate over each digit.
- We initialize two counters, `even` and `odd`, to keep track of the number of even and odd digits, respectively.
- We use a `for` loop to iterate over each digit in the number.
- Inside the loop, we use `parseInt(num[i])` to convert the character at index `i` to an integer.
- We then check if the digit is even by using the modulo operator (`%`). If the remainder is 0, the digit is even, and we increment the `even` counter. If the remainder is 1, the digit is odd, and we increment the `odd` counter.
- Finally, we return an array containing the counts of even and odd digits, respectively.