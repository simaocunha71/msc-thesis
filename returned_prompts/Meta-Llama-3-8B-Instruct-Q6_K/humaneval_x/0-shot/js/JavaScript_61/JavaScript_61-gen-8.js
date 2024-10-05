```
const correctBracketing = (brackets) => {
  let count = 0;
  for (let i = 0; i < brackets.length; i++) {
    if (brackets[i] === '(') {
      count++;
    } else if (brackets[i] === ')') {
      if (count === 0) return false;
      count--;
    }
  }
  return count === 0;
};
```


Explanation:
The function iterates over the string of brackets, incrementing a counter whenever it encounters an opening bracket and decrementing the counter whenever it encounters a closing bracket. If the counter ever becomes negative, it means that there are more closing brackets than opening brackets, so the function immediately returns `false`. If the function iterates over the entire string without encountering any issues, it checks if the counter is still at zero. If it is, the function returns `true`, indicating that every opening bracket had a corresponding closing bracket. Otherwise, it returns `false`.