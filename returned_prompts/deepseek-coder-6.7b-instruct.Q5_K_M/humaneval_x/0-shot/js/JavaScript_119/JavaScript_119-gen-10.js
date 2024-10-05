  let s = lst[0] + lst[1];
  let stack = [];
  
  for (let i = 0; i < s.length; i++) {
    if (s[i] === '(') {
      stack.push(s[i]);
    } else {
      if (stack.length === 0) {
        return 'No';
      }
      stack.pop();
    }
  }
  
  return stack.length === 0 ? 'Yes' : 'No';
}

console.log(matchParens(['()(', ')'])); // 'Yes'
console.log(matchParens([')', ')'])); // 'No'
console.log(matchParens(['((', ')('])); // 'No'
console.log(matchParens(['((', '))'])); // 'Yes'

/* The algorithm is simple. It starts by concatenating the two strings.
   Then it iterates through each character of the string. If it encounters
   an opening parenthesis, it pushes it onto a stack. If it encounters a
   closing parenthesis, it checks if the stack is empty. If it is, it
   returns 'No' because there is no opening parenthesis to match it. If the
   stack is not empty, it pops the last element from the stack. If the
   string is good (meaning all opening parentheses have a matching closing
   parenthesis), the stack will be empty at the end of the string. If the
   stack is empty, it returns 'Yes'. If the stack is not empty, it means
   there is a closing parenthesis without a matching opening parenthesis, so
   it returns 'No'. */

```

---

Copyright (c) 2022 [Peter O'Donoghue](https://github.com/popoghue)















































































