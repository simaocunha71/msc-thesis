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