    public boolean correctBracketing(String brackets) {
        Stack<Character> stack = new Stack<>();
        for (char bracket : brackets.toCharArray()) {
            if (bracket == '(') {
                stack.push(')');
            } else if (bracket == ')') {
                if (stack.isEmpty() || stack.pop() != ')') {
                    return false;
                }
            }
        }
        return stack.isEmpty();
    }

Explanation:

1. We use a stack to keep track of the opening brackets.
2. We iterate over the string, and for each character:
   - If it's an opening bracket, we push the corresponding closing bracket onto the stack.
   - If it's a closing bracket, we check if the stack is empty or if the top of the stack doesn't match the current closing bracket. If either condition is true, we return false.
3. After iterating over the entire string, we check if the stack is empty. If it is, it means every opening bracket had a corresponding closing bracket, so we return true. If the stack is not empty, it means there were some opening brackets without corresponding closing brackets, so we return false.