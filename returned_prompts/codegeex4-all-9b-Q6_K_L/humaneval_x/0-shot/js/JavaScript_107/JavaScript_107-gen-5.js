```js
const evenOddPalindrome = (n) => {
    let even = 0, odd = 0;
    for (let i = 1; i <= n; i++) {
        let str = i.toString();
        let reversedStr = str.split('').reverse().join('');
        if (str === reversedStr) {
            if (i % 2 === 0) {
                even++;
            } else {
                odd++;
            }
        }
    }
    return [even, odd];
};
```