        String str1 = lst.get(0);
        String str2 = lst.get(1);
        Stack<Character> stack = new Stack<>();

        for(int i = 0; i < str1.length(); i++){
            char c = str1.charAt(i);
            if(c == '(') stack.push(c);
            else if(c == ')'){
                if(stack.isEmpty()) return "No";
                else stack.pop();
            }
        }

        for(int i = 0; i < str2.length(); i++){
            char c = str2.charAt(i);
            if(c == '(') stack.push(c);
            else if(c == ')'){
                if(stack.isEmpty()) return "No";
                else stack.pop();
            }
        }

        return stack.isEmpty() ? "Yes" : "No";
    }

}

// Time Complexity: O(n)
// Space Complexity: O(n)

The solution is using the concept of stack. We are pushing open brackets into the stack and popping them off when we encounter a closed bracket. If at any point we encounter a closed bracket and the stack is empty, we return "No". If the stack is empty after traversing both strings, we return "Yes".

The reason it works is because it ensures that we're only closing brackets that we've opened. If we encounter a closed bracket when the stack is empty, that means we're trying to close a bracket that we never opened, which is not balanced.

This solution also takes care of the scenario where the second string starts with a closed bracket. It would not be good to start with a closed bracket, so we're returning "No" in this case.

It's also worth noting that this solution assumes that the strings only contain parentheses and no other characters. If this is not the case, we would need to update the solution to handle these additional characters.

Overall, this solution is a good approach to solve the problem.

