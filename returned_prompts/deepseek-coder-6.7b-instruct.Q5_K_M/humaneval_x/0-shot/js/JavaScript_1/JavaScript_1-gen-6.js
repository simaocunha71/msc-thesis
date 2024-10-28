  // remove spaces and convert to array
  const arr = paren_string.replace(/\s/g, '').split('');
  const stack = [];
  const result = [];
  let temp = '';
  
  for(let i = 0; i < arr.length; i++) {
    if (arr[i] === '(') {
      stack.push(arr[i]);
      temp += arr[i];
    } else if (arr[i] === ')') {
      stack.pop();
      temp += arr[i];
      if (stack.length === 0) {
        result.push(temp);
        temp = '';
      }
    }
  }
  return result;
}

console.log(separateParenGroups('(  )  (( ))  (( )( ))')); // ['()', '(())', '(()())']

*/

/* Expected output: 
['()', '(())', '(()())']
*/

```

## 4. **Palindrome Checker**

```js
/*
