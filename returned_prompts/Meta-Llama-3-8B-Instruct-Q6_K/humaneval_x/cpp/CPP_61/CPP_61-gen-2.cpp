    int count = 0;
    for(int i = 0; i < brackets.length(); i++){
        if(brackets[i] == '('){
            count++;
        }
        if(brackets[i] == ')'){
            if(count == 0){
                return false;
            }
            count--;
        }
    }
    if(count != 0){
        return false;
    }
    return true;
}

int main(){
    printf("%d\n", correct_bracketing("("));
    printf("%d\n", correct_bracketing("()"));
    printf("%d\n", correct_bracketing("(()())"));
    printf("%d\n", correct_bracketing(")(()"));
    return 0;
}

