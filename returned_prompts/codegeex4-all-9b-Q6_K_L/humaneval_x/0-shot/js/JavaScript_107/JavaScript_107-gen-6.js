```javascript
const evenOddPalindrome = (n) => {
    let even = 0, odd = 0;
    for (let i = 1; i <= n; i++) {
        if (i % 2 === 0) {
            even += isPalindrome(i);
        } else {
            odd += isPalindrome(i);
        }
    }
    return [even, odd];
};

const isPalindrome = (num) => {
    let str = num.toString();
    let len = str.length;
    for (let i = 0; i < len / 2; i++) {
        if (str[i] !== str[len - 1 - i]) {
            return 0;
        }
    }
    return 1;
};
```
