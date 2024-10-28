Here is the JavaScript code to solve the problem:

```javascript
const isHappy = (s) => {
    if (s.length < 3) {
        return false;
    }
    for (let i = 0; i < s.length - 2; i++) {
        if (s[i] === s[i + 1] || s[i] === s[i + 2] || s[i + 1] === s[i + 2]) {
            return false;
        }
    }
    return true;
};
```

Explanation:
The code first checks if the length of the string is less than 3. If it is, it returns `false` because a string of length less than 3 cannot be happy. Then, it iterates over the string, checking every 3 consecutive letters. If any 3 consecutive letters are the same, it returns `false`. If it checks all 3 consecutive letters and none of them are the same, it returns `true`, indicating that the string is happy.