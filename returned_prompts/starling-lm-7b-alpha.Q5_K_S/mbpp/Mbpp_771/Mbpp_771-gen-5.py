```
# Python3 program to check if the given
# expression is balanced or not 

# Returns true if the given expression is 
# balanced or false 
def check_expression(exp): 
    stack = [] 
  
    # Traverse the expression 
    for i in range(len(exp)): 
        # If the current character is an 
        # opening brace, push it to the stack 
        if (exp[i] == "(" or exp[i] == "[" or exp[i] == "{"): 
            stack.append(exp[i]) 
  
        # If the current character is a closing 
        # brace, then pop the top element from 
        # the stack 
        elif (exp[i] == ")" or exp[i] == "]" or exp[i] == "}"): 
            if (len(stack) == 0 or 
               (exp[i] != ")" and stack[-1] != "(" or 
                exp[i] != "]" and stack[-1] != "[" or 
                exp[i] != "}" and stack[-1] != "{")): 
                return False 
  
            # Pop the top element from the stack 
            stack.pop() 
  
    # Check Empty Stack 
    return (len(stack) == 0)
```

Explanation:
This function `check_expression` takes a string as input and returns True if the given expression is balanced or False if the expression is not balanced.

The function works by using a stack to keep track of opening braces. If an opening brace is encountered, it is pushed onto the stack. If a closing brace is encountered, the top element of the stack is popped and compared to the closing brace. If the closing brace does not match the top element of the stack, the function returns False.

At the end of the function, if the stack is empty, it means all the opening braces have been matched with closing braces and the function returns True. Otherwise, if the stack is not empty, it means there are unmatched opening braces and the function returns False.

The function uses the `len()` function to check if the stack is empty or not.

