    int opening = 0; // count of opening brackets
    for(int i = 0; i < brackets.length(); i++) {
        if(brackets[i] == '(') {
            opening++; // increment the count of opening brackets
        }
        else if(brackets[i] == ')') {
            if(opening > 0) {
                opening--; // decrement the count of opening brackets
            }
            else {
                return false; // if there is no corresponding opening bracket, return false
            }
        }
    }
    if(opening > 0) {
        return false; // if there are remaining opening brackets, return false
    }
    return true; // if every opening bracket has a corresponding closing bracket, return true
}

int main(){
    printf("%d\n", correct_bracketing("(")); // prints 0
    printf("%d\n", correct_bracketing("()")); // prints 1
    printf("%d\n", correct_bracketing("(()())")); // prints 1
    printf("%d\n", correct_bracketing(")((")); // prints 0
    return 0;
}
