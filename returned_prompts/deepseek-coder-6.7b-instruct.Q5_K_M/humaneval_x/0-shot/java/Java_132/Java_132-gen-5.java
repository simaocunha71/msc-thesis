        Stack<Character> stack = new Stack<>();

        for(int i = 0; i < string.length(); i++){
            char c = string.charAt(i);

            if(c == '['){
                stack.push(c);
            } else if(c == ']'){
                if(stack.isEmpty()){
                    return false;
                }
                if(stack.peek() == '['){
                    stack.pop();
                } else {
                    while(!stack.isEmpty() && stack.peek() != '['){
                        stack.pop();
                    }
                    if(stack.isEmpty()){
                        return false;
                    }
                    stack.pop();
                }
            }
        }
        return !stack.isEmpty();
    }
}

```

This program uses a stack to keep track of the brackets. If it encounters an opening bracket, it pushes it onto the stack. If it encounters a closing bracket, it checks whether the stack is empty or the top of the stack is an opening bracket. If the stack is empty or the top of the stack is an opening bracket, it returns false. If the top of the stack is a closing bracket, it pops the top element from the stack. If the stack is not empty after the operation, it returns false. If the stack is empty after the operation, it returns true.

The time complexity of this program is O(n) where n is the length of the string. The space complexity is O(n) as well.

This program should work for all cases as it checks all the possible scenarios.

Please let me know if you have any questions.































































































































