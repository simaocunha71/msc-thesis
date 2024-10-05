  let str1 = lst[0];
  let str2 = lst[1];
  let stack = [];

  for (let i = 0; i < str1.length; i++) {
    if (str1[i] === '(') {
      stack.push(str1[i]);
    } else {
      if (stack.length === 0 || stack[stack.length - 1] !== '(') {
        return 'No';
      } else {
        stack.pop();
      }
    }
  }

  for (let i = 0; i < str2.length; i++) {
    if (str2[i] === '(') {
      stack.push(str2[i]);
    } else {
      if (stack.length === 0 || stack[stack.length - 1] !== '(') {
        return 'No';
      } else {
        stack.pop();
      }
    }
  }

  return stack.length === 0 ? 'Yes' : 'No';
}

console.log(matchParens(['()(', ')'])) // 'Yes'
console.log(matchParens([')', ')'])) // 'No'
```

## Problem 5:
