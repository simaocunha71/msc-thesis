Here is the solution:

```javascript
const reverseDelete = (s, c) => {
  let result = '';
  for (let char of s) {
    if (!c.includes(char)) {
      result += char;
    }
  }
  return [result, result === result.split('').reverse().join('')];
};
```


Explanation:
The function takes two strings `s` and `c` as input. It iterates over each character `char` in `s`. If `char` is not present in `c`, it adds `char` to the `result` string. Finally, it checks if the `result` string is the same when reversed (i.e., a palindrome) and returns a tuple containing the `result` string and a boolean indicating whether it's a palindrome.