Here is the solution using JavaScript:

```javascript
function hexKey(num) {
    let count = 0;
    for (let i = 0; i < num.length; i++) {
        let char = num[i];
        if (char >= '2' && char <= '7') {
            count++;
        } else if (char === 'B' || char === 'D' || char === 'F') {
            count++;
        }
    }
    return count;
}
```

This function iterates over each character in the input string. If the character is a digit between 2 and 7 (inclusive), or if it is the character 'B', 'D', or 'F' (which correspond to the decimal values 11, 13, and 15, respectively), it increments the count. Finally, the function returns the count.