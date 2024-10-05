You can solve this problem by converting the number to a string and iterating over each character. If the character is an odd digit, you multiply the current product by that digit. If all the digits are even, you return 0.
Here's the JavaScript code that solves this problem:

```javascript
const digits = (n) => {
    let product = 1;
    let allEven = true;
    let str = n.toString();
    for (let i = 0; i < str.length; i++) {
        let digit = parseInt(str[i]);
        if (digit % 2 !== 0) {
            product *= digit;
            allEven = false;
        }
    }
    return allEven ? 0 : product;
}
```

You can test this function with the following examples:

```javascript
console.log(digits(1));  // 1
console.log(digits(4));  // 0
console.log(digits(235));  // 15
```