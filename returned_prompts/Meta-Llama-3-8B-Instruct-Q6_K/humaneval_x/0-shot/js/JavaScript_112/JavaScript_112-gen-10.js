```javascript
const reverseDelete = (s, c) => {
    let newStr = s.split('');
    for(let i = 0; i < c.length; i++) {
        for(let j = 0; j < newStr.length; j++) {
            if(newStr[j] === c[i]) {
                newStr.splice(j, 1);
                j--;
            }
        }
    }
    let result = newStr.join('');
    let isPalindrome = result === result.split('').reverse().join('');
    return [result, isPalindrome];
};
```


This code first creates a new string by splitting the input string `s` into an array of characters. Then, it iterates over each character in the string `c` and checks if any character in the array of characters is equal to the current character in `c`. If it finds a match, it removes that character from the array.

After all characters in `c` have been checked, it joins the remaining characters back into a string and checks if the resulting string is a palindrome by comparing it to its reverse. The result is returned as a tuple containing the resulting string and a boolean indicating whether the string is a palindrome.