    // initialize a stack with empty string
    string stack = "";
    for(int i = 0; i < brackets.length(); i++){
        // if the character is an opening bracket, push it into the stack
        if(brackets[i] == '('){
            stack += '(';
        }
        // if the character is a closing bracket, pop the stack if it's not empty
        else if(brackets[i] == ')'){
            if(stack.empty()){
                return false;  // there's no corresponding opening bracket
            }else{
                stack.pop_back();  // remove the top element from the stack
            }
        }
    }
    // if there are remaining opening brackets in the stack, return false
    return stack.empty();
}

int main(int argc, char* argv[]) {
    printf("%d\n", correct_bracketing("()"));  // true
    printf("%d\n", correct_bracketing("("));  // false
    printf("%d\n", correct_bracketing("(()())"));  // true
    printf("%d\n", correct_bracketing(")(())"));  // false
    return 0;
}
