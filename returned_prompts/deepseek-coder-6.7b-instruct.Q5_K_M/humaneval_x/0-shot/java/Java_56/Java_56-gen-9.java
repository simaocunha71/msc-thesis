        Stack<Character> stack = new Stack<Character>();
        for(char c : brackets.toCharArray()){
            if(c == '<'){
                stack.push(c);
            }else{
                if(stack.isEmpty()){
                    return false;
                }
                if(stack.peek() == '<'){
                    stack.pop();
                }else{
                    return false;
                }
            }
        }
        return stack.isEmpty();
    }
}

Explanation:
This solution uses a stack to keep track of the brackets. When it encounters an opening bracket, it pushes it onto the stack. When it encounters a closing bracket, it checks if the top of the stack is an opening bracket. If it is, it removes the opening bracket from the stack. If the stack is empty at the end, it means that all opening brackets have matching closing brackets, so it returns true. If the stack is not empty at the end, it means that there are unmatched opening brackets, so it returns false.

The time complexity of this solution is O(n), where n is the length of the string. This is because it iterates through the string once. The space complexity is also O(n), where n is the length of the string. This is because in the worst case, all characters in the string could be opening brackets and the stack would need to store all of them.
