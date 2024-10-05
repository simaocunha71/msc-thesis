import java.util.*;
import java.lang.*;

class Solution {
    /**
    brackets is a string of "<" and ">".
    return True if every opening bracket has a corresponding closing bracket.
    
    >>> correctBracketing("<")
    false
    >>> correctBracketing("<>")
    true
    >>> correctBracketing("<<><>>")
    true
    >>> correctBracketing("><<>")
    false
     */
    public boolean correctBracketing(String brackets) {
        //create a stack to keep track of the brackets
        Stack<Character> stack = new Stack<Character>();
        
        //loop through the string
        for(int i = 0; i < brackets.length(); i++){
            //if the current bracket is an opening bracket, push it onto the stack
            if(brackets.charAt(i) == '<'){
                stack.push(brackets.charAt(i));
            }
            //if the current bracket is a closing bracket
            else if(brackets.charAt(i) == '>'){
                //if the stack is empty or the top of the stack is not an opening bracket, return false
                if(stack.isEmpty() || stack.peek() != '<'){
                    return false;
                }
                //otherwise, pop the opening bracket off the stack
                else{
                    stack.pop();
                }
            }
        }
        
        //if the stack is empty, return true. otherwise, return false
        return stack.isEmpty();
    }
}

print(Solution.correctBracketing("<"))
print(Solution.correctBracketing("<>"))
print(Solution.correctBracketing("<<><>>"))
print(Solution.correctBracketing("><<>"))
print(Solution.correctBracketing("><<>>"))
print(Solution.correctBracketing("><<>><>>"))