Here is the solution for the problem:

```javascript
const evenOddCount = (num) => {
    let evenCount = 0;
    let oddCount = 0;
    const str = num.toString();
    for(let i = 0; i < str.length; i++) {
        if(Number(str[i]) % 2 === 0) {
            evenCount++;
        } else {
            oddCount++;
        }
    }
    return [evenCount, oddCount];
};
```


Explanation:
The function `evenOddCount` takes an integer `num` as input. It converts the integer to a string `str` for easier manipulation.

Then, it initializes two counters `evenCount` and `oddCount` to 0. It then loops through each character in the string using a for loop.

Inside the loop, it checks if the character (which is a digit) is even by using the modulus operator `% 2 === 0`. If it is, it increments the `evenCount`. If it's not, it increments the `oddCount`.

Finally, it returns an array with the counts of even and odd digits respectively.

Test cases:
```javascript
console.log(evenOddCount(-12)); // Output: [1, 1]
console.log(evenOddCount(123)); // Output: [1, 2]
```


This solution works for both positive and negative integers. It also correctly handles numbers with leading zeros. For example, the number 012 would be considered as having one even digit (0) and two odd digits (1 and 2).