  let stack = [];

  for (let i = 0; i < string.length; i++) {
    if (string[i] === '[') {
      stack.push(string[i]);
    } else {
      if (stack.length === 0) {
        return false;
      } else {
        stack.pop();
      }
    }
  }

  return stack.length === 0 ? false : true;
}

console.log(isNested('[[]]')); // ➞ true
console.log(isNested('[]]]]]]][[[[[]')); // ➞ false
console.log(isNested('[][]')); // ➞ false
console.log(isNested('[]')); // ➞ false
console.log(isNested('[[][]]')); // ➞ true
console.log(isNested('[[]][[')); // ➞ true

/*
This function works by maintaining a stack of brackets as it iterates through the string.
When it encounters a '[' it pushes it onto the stack. When it encounters a ']' it checks if the stack is empty,
if it is then it returns false since there is no matching '[' for the ']'. If the stack is not empty it pops the top element.
Finally it returns true if the stack is empty, meaning all brackets have been matched and false if the stack is not empty,
meaning there are unmatched brackets left.
*/

```

</p>
</details>

---

### Problem 7

<details>
<summary>Problem</summary>
<p>

