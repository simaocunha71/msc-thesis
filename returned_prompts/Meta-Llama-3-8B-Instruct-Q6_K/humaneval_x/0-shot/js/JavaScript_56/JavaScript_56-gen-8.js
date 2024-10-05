```javascript
const correctBracketing = (brackets) => {
  let count = 0;
  for (let i = 0; i < brackets.length; i++) {
    if (brackets[i] === "<") {
      count++;
    } else if (brackets[i] === ">") {
      count--;
      if (count < 0) {
        return false;
      }
    }
  }
  return count === 0;
};
```


Explanation:
The function `correctBracketing` takes a string of "<" and ">" as an argument. It initializes a counter `count` to 0. Then it iterates through the string. If it encounters an opening bracket "<", it increments the `count`. If it encounters a closing bracket ">", it decrements the `count`. If the `count` becomes negative, it means there are more closing brackets than opening brackets, so the function returns `false`. Finally, if the `count` is 0 after iterating through the entire string, it means every opening bracket has a corresponding closing bracket, so the function returns `true`. If the `count` is not 0, it means there are some opening brackets without corresponding closing brackets, so the function returns `false`.