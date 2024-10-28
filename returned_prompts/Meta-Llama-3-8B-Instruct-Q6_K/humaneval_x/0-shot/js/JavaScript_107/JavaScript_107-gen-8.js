```
function evenOddPalindrome(n) {
    let even = 0;
    let odd = 0;

    for (let i = 1; i <= n; i++) {
        let str = i.toString();
        let isPalindrome = true;

        for (let j = 0; j < str.length / 2; j++) {
            if (str[j] !== str[str.length - 1 - j]) {
                isPalindrome = false;
                break;
            }
        }

        if (isPalindrome && i % 2 === 0) {
            even++;
        } else if (isPalindrome) {
            odd++;
        }
    }

    return [even, odd];
}
```


The above code defines a function `evenOddPalindrome` that takes a positive integer `n` as input. It initializes two variables `even` and `odd` to 0, which will be used to store the count of even and odd integer palindromes, respectively.

The function then iterates from 1 to `n` using a `for` loop. For each integer `i`, it converts it to a string `str` and checks if it's a palindrome by comparing the characters from the start and end of the string. If `i` is a palindrome and even, it increments the `even` count; if `i` is a palindrome but odd, it increments the `odd` count.

Finally, the function returns an array containing the counts of even and odd integer palindromes.

For example, if `n` is 3, the function will return `[1, 2]`, indicating that there is one even integer palindrome (2) and two odd integer palindromes (1 and 3). If `n` is 12, the function will return `[4, 6]`, indicating that there are four even integer palindromes (2, 4, 6, and 8) and six odd integer palindromes (1, 3, 5, 7, 9, and 11).