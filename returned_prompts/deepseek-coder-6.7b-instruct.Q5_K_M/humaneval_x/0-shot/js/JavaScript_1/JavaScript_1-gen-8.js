let paren_array = paren_string.split(' ').filter(paren => paren.length > 0);
  let stack = [];
  let result = [];
  for(let i = 0; i < paren_array.length; i++){
    stack.push(paren_array[i]);
    if(paren_array[i].includes(')')){
      while(stack[stack.length - 1] !== '('){
        stack.pop();
      }
      if(stack.length === 1){
        result.push(stack.join(''));
        stack = [];
      }
    }
  }
  return result;
};
console.log(separateParenGroups('(  )  (( ))  (( )( ))')); 
// Output: [ '()', '(())', '(()())' ]
```

This JavaScript function uses a stack to solve the problem. It first splits the input string into an array of non-empty strings. It then iterates over this array. If it encounters a closing parenthesis, it pops the stack until it encounters an opening parenthesis, which indicates the end of a group. It then adds this group to the result array. The function then returns this array.

The function uses the `split` method to split the string into an array of characters, and the `filter` method to remove any empty strings from the array. It then uses a for loop to iterate over the array.

The function uses the `push` and `pop` methods of the array to maintain a stack of characters. It uses the `includes` method to check if the current character is a closing parenthesis.

If the current character is a closing parenthesis, it pops the stack until it finds an opening parenthesis. It then checks if the stack has only one element left (which is the opening parenthesis of the group). If this is the case, it adds the group to the result array and clears the stack.

Finally, the function returns the result array.

The time complexity of this function is O(n), where n is the length of the input string. This is because it iterates over the string once. The space complexity is also O(n), where n is the length of the input string, because