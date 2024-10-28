```javascript
function isHappy(s) {
    if (s.length < 3) return false;
    for (let i = 0; i < s.length - 2; i++) {
        if (s.slice(i, i + 3).split('').sort().join('') === s.slice(i, i + 3)) return false;
    }
    return true;
}
```


The function `isHappy(s)` takes a string `s` as an argument and returns a boolean indicating whether the string is "happy" or not.

The function first checks if the length of the string is less than 3. If it is, it returns `false` because a happy string must have at least 3 characters.

Then, it uses a loop to check every 3 consecutive characters in the string. It uses the `slice()` method to extract a slice of the string starting from the current index `i` and ending at `i + 3`. It then splits this slice into an array of characters using the `split('')` method, sorts this array using the `sort()` method, and joins it back into a string using the `join('')` method.

It then checks if this sorted string is equal to the original slice of the string. If it is, it means that the 3 consecutive characters are the same, and the function returns `false`.

If the function finishes checking all 3-character slices without finding any duplicates, it returns `true`, indicating that the string is "happy".