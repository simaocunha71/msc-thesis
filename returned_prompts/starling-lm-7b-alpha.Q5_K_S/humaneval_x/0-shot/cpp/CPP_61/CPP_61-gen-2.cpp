    int count = 0;
    for(int i = 0; i < brackets.length(); i++){
        if(brackets[i] == '(')
            count++;
        else if(brackets[i] == ')')
            count--;
        if(count < 0)
            return false;
    }
    if(count == 0)
        return true;
    else
        return false;
}




/*
A function named correct_bracketing that takes a string and returns true if all opening brackets have corresponding closing brackets.

For example:
>>> correct_bracketing("(")
false
>>> correct_bracketing("()")
true
>>> correct_bracketing("(()())")
true
>>> correct_bracketing(")(()")
false

The function should return false if there's a bracket without a matching pair. It should return false if the opening brackets don't appear before the closing brackets.

The function should return true if all opening brackets have corresponding closing brackets and they appear in the correct order.

You can assume that the input will only contain '(' and ')'.

Here are some tips to get you started:

To count the number of opening brackets, initialize a counter to 0 and increment it each time you see an opening bracket.
To count the number of closing brackets, initialize a counter to 0 and decrement it each time you see a closing bracket.
At the end of the function, if the counter is 0, then all opening brackets have closing brackets. Otherwise, some opening brackets are missing closing brackets.
*/
























































































































