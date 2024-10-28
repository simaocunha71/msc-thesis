  const stack = [];
  for (let i = 0; i < brackets.length; i++) {
    if (brackets[i] === '(') {
      stack.push('(');
    } else {
      if (stack.length === 0) {
        return false;
      }
      stack.pop();
    }
  }
  return stack.length === 0;

};





/*
The correctBracketing function will return true if every opening bracket has a corresponding closing bracket. Otherwise, it will return false.

The function works by iterating over each character in the string and pushing each opening bracket onto a stack. If an opening bracket is encountered, it is added to the stack. If a closing bracket is encountered, the function checks if the stack is empty. If the stack is empty, this means there is no corresponding opening bracket, so the function returns false. Otherwise, the function pops the top bracket off the stack, removing it.

After iterating through all the characters, the function checks if the stack is empty. If the stack is empty, this means all opening brackets have a corresponding closing bracket, and the function returns true. Otherwise, there are unmatched opening brackets, so the function returns false.

The time complexity of the function is O(n), where n is the length of the input string, as the function iterates through the string once. The space complexity is O(n) as well, as the function uses a stack that can hold up to n elements.

The function can be used to check if the parentheses in a given string are correctly balanced.

Explanation of the code:

The function starts by initializing an empty stack.

The function then iterates over each character in the input string using a for loop. For each character, the function checks if it is an opening bracket (a parenthesis '('). If it is, the function pushes the character onto the stack using the push method. If it is not an opening bracket, the function checks if the stack is empty using the length property. If the stack is empty, this means there is no corresponding opening bracket, so the function returns false immediately. Otherwise, the function pops the top bracket off the stack using the pop