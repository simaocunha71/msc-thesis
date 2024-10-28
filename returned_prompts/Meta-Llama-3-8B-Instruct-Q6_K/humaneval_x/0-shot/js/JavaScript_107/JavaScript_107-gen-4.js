```
function evenOddPalindrome(n) {
    let evenCount = 0;
    let oddCount = 0;
    for (let i = 1; i <= n; i++) {
        let str = i.toString();
        if (str === str.split('').reverse().join('')) {
            if (+str % 2 === 0) evenCount++;
            else oddCount++;
        }
    }
    return [evenCount, oddCount];
}
```


Explanation:
We loop through all numbers from 1 to n. For each number, we convert it to a string and check if it's a palindrome by comparing it with its reverse. If it's a palindrome, we check if the number is even or odd and increment the corresponding counter. Finally, we return the counts of even and odd palindromes.