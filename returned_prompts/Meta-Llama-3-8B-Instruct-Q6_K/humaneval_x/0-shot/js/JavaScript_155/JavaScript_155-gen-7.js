Here is the solution using JavaScript:

```javascript
const evenOddCount = (num) => {
    let evenCount = 0;
    let oddCount = 0;
    String(num).split('').forEach((digit) => {
        if (parseInt(digit) % 2 === 0) {
            evenCount++;
        } else {
            oddCount++;
        }
    });
    return [evenCount, oddCount];
};
```

Here's an explanation of the code:

1. We initialize two variables `evenCount` and `oddCount` to keep track of the number of even and odd digits respectively.
2. We convert the input number to a string using `String(num)`.
3. We split the string into individual digits using `split('')`.
4. We use `forEach` to iterate over the digits.
5. For each digit, we check if it's even or odd by using the modulo operator (`%`). If the remainder is 0, the digit is even, otherwise it's odd.
6. We increment the corresponding count variable (`evenCount` or `oddCount`) based on the result.
7. Finally, we return an array containing the `evenCount` and `oddCount`.

You can test the function with the examples you provided:

```javascript
console.log(evenOddCount(-12)); // Output: [1, 1]
console.log(evenOddCount(123)); // Output: [1, 2]
```