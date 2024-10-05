        Stack<Character> stack = new Stack<>();

        for (char c : string.toCharArray()) {
            if (c == '[') {
                stack.push(c);
            } else if (c == ']') {
                if (stack.isEmpty()) {
                    return false;
                }
                if (stack.peek() == '[') {
                    stack.pop();
                } else {
                    while (!stack.isEmpty() && stack.peek() != '[') {
                        stack.pop();
                    }
                    if (stack.isEmpty()) {
                        return false;
                    }
                    stack.pop();
                }
            }
        }

        return !stack.isEmpty();
    }
}

The function isNested uses a stack to track the nested brackets. 

If the input string contains a '[', it is pushed into the stack. 

If the input string contains a ']', it pops the top element from the stack. 

If the top element is '[', it means there is a valid subsequence of brackets. 

If the top element is not '[', it pops all elements until it finds a '[' or the stack is empty. 

If after popping all elements, the stack is still not empty, it means there is another valid subsequence of brackets. 

Finally, if the stack is not empty, it means there are still some unpaired '[' in the string, so it returns false.

If the stack is empty, it means there is no valid subsequence of brackets, so it returns false.

The function isNested will return true only if there is at least one valid subsequence of brackets in the string.

Note: This function assumes that the input string only contains square brackets and does not contain any other characters.
*/

// Test Cases:

// Test Case 1:
// Input: "[[]]"
// Expected Output: true

// Test Case 2:
// Input: "[]]]]]]][[[[[]"
// Expected Output: false

// Test Case 3:
// Input: "[][]"
// Expected Output: false

// Test Case 4:
