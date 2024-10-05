        Stack<Character> stack = new Stack<>();

        for (int i = 0; i < brackets.length(); i++) {
            char c = brackets.charAt(i);

            if (c == '<') {
                stack.push(c);
            } else if (c == '>') {
                if (stack.isEmpty()) {
                    return false;
                }
                stack.pop();
            }
        }

        return stack.isEmpty();
    }
}


A: 
import java.util.*;
import java.lang.*;

class Solution 
{
    public boolean correctBracketing(String brackets) 
    {
        Stack<Character> stack = new Stack<>();

        for (int i = 0; i < brackets.length(); i++) 
        {
            char c = brackets.charAt(i);

            if (c == '<') 
            {
                stack.push(c);
            } 
            else if (c == '>') 
            {
                if (stack.isEmpty()) 
                {
                    return false;
                }
                stack.pop();
            }
        }

        return stack.isEmpty();
    }

    public static void main(String[] args) 
    {
        Solution s = new Solution();
        System.out.println(s.correctBracketing("<<><>>"));  // Should print: true
        System.out.println(s.correctBracketing("><<>"));  // Should print: false
    }
}

Explanation:

The function correctBracketing() uses a stack to keep track of the opening brackets. It iterates through the input string, pushing each '<' onto the stack and popping from the stack whenever it encounters a '>'. If the stack is empty and it encounters a '>', it means there is no matching opening bracket and the function returns false. If the stack is empty after processing the entire string, the function returns true, indicating that all opening brackets have been matched by closing brackets.

In the main method, we create an instance of the Solution class and call the correctBracketing()