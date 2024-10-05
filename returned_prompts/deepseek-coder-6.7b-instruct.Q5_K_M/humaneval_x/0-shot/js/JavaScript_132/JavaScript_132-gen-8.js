  let stack = [];
  for(let i=0; i<string.length; i++){
    if(string[i] === '['){
      stack.push(string[i]);
    }
    else{
      if(stack.length === 0) return false;
      stack.pop();
    }
    if(stack.length > 1) return true;
  }
  return false;
}
console.log(isNested('[[]]')); // ➞ true
console.log(isNested('[]]]]]]][[[[[]')); // ➞ false
console.log(isNested('[][]')); // ➞ false
console.log(isNested('[]')); // ➞ false
console.log(isNested('[[][]]')); // ➞ true
console.log(isNested('[[]][[')); // ➞ true
```

Explanation:
This problem can be solved by using stack data structure.
We will iterate through the input string, and every time we encounter an opening bracket, we push it to the stack.
If we encounter a closing bracket, we pop an element from the stack.
If at any point, the stack has more than one element, that means we have found a nested bracket, so we return true.
If we finish iterating through the string and the stack is empty, that means there are no nested brackets, so we return false.













































































































































































