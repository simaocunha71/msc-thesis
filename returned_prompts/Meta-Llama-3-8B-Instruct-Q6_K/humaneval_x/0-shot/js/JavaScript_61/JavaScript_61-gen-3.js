```
const correctBracketing = (brackets) => {
  let stack = [];
  for (let bracket of brackets) {
    if (bracket === '(') {
      stack.push(')');
    } else if (bracket === ')') {
      if (stack.length === 0 || stack.pop() !== ')') {
        return false;
      }
    }
  }
  return stack.length === 0;
};
```


Explanation:
The function `correctBracketing` takes a string of brackets as input and returns a boolean indicating whether every opening bracket has a corresponding closing bracket.

We use a stack to keep track of the opening brackets. When we encounter an opening bracket `(`, we push the corresponding closing bracket `)` onto the stack. When we encounter a closing bracket `)`, we check if the stack is empty or if the top of the stack does not match the closing bracket `)`. If either condition is true, we return `false`.

After processing all the brackets, we check if the stack is empty. If it is not empty, it means there are unmatched opening brackets, so we return `false`. Otherwise, we return `true` indicating that every opening bracket has a corresponding closing bracket.

The time complexity is O(n), where n is the length of the input string, because we process each character once. The space complexity is O(n) in the worst case when the input string consists only of opening brackets. In the average case, the space complexity is O(1) when the input string has a balanced number of opening and closing brackets.