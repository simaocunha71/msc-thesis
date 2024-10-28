The solution to this problem can be achieved by using a simple loop to check the length of the string and every 3 consecutive letters. Here is the JavaScript code for the problem:

```javascript
const isHappy = (s) => {
  if (s.length < 3) return false;
  for (let i = 0; i <= s.length - 3; i++) {
    const threeConsecutive = s.substring(i, i + 3);
    if (threeConsecutive.includes(threeConsecutive[0]) || threeConsecutive.includes(threeConsecutive[1]) || threeConsecutive.includes(threeConsecutive[2])) {
      return false;
    }
  }
  return true;
};
```

This function first checks if the string's length is less than 3. If it is, the function immediately returns false. Then, it loops through the string and checks every 3 consecutive letters. If any of these 3 consecutive letters are repeated, the function returns false. If the function finishes the loop without finding any repeated 3 consecutive letters, it returns true. This means the string is happy.