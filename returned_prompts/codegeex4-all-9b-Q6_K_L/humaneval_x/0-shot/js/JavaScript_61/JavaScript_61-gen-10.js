```js
  const opening = '(){}[]';
  const closing = '())}]';
  let stack = [];
  for (let i = 0; i < brackets.length; i++) {
    if (opening.includes(brackets[i])) {
      stack.push(brackets[i]);
    } else if (closing.includes(brackets[i])) {
      const last = stack.pop();
      if (last === undefined) {
        return false;
      } else if (closing.indexOf(brackets[i]) !== opening.indexOf(last)) {
        return false;
      }
    }
  }
  return stack.length === 0;
};
```