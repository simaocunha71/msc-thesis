    int open_count = 0;
    for(int i = 0; i < brackets.length(); i++){
        if(brackets[i] == '(') open_count++;
        if(brackets[i] == ')') open_count--;
        if(open_count < 0) return false;
    }
    return open_count == 0;
}

B:
    int open_count = 0;
    for(int i = 0; i < brackets.length(); i++){
        if(brackets[i] == '(') open_count++;
        if(brackets[i] == ')'){
            if(open_count == 0) return false;
            open_count--;
        }
    }
    return open_count == 0;
}

C:
    bool correct_bracketing(string brackets){
        stack<char> bracket_stack;
        for(int i = 0; i < brackets.length(); i++){
            if(brackets[i] == '(') bracket_stack.push('(');
            if(brackets[i] == ')'){
                if(bracket_stack.empty()) return false;
                bracket_stack.pop();
            }
        }
        return bracket_stack.empty();
    }
}

Explanation:
A) This solution uses a counter to keep track of the number of open brackets encountered so far. It increments the counter when it encounters an open bracket and decrements it when it encounters a close bracket. If the counter ever becomes negative, it means there are more close brackets than open brackets, so it returns false. If it reaches the end of the string and the counter is zero, it means every open bracket had a corresponding close bracket, so it returns true.

B) This solution is similar to A, but it checks if the open_count is zero before decrementing it when it encounters a close bracket. This is to avoid returning false when it encounters a close bracket that corresponds to a previously encountered open bracket.

C) This solution uses a stack to keep track of the open brackets. It pushes an open bracket onto the stack when it encounters one, and pops one off the stack when it encounters a close bracket. If it ever tries to pop a close bracket when the stack is empty, it means there are more close brackets than open brackets, so it returns false. If it reaches the end of the string and the stack is empty, it means every open bracket had a corresponding close bracket, so it returns true. This solution is more efficient than A and B because it uses a stack to keep track of the open brackets, which allows it to avoid having to iterate over the entire string again at the