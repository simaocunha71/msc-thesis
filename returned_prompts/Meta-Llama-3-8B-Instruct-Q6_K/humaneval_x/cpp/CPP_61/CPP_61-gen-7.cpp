    int count = 0;
    for(int i = 0; i < brackets.length(); i++){
        if(brackets[i] == '('){
            count++;
        }
        else if(brackets[i] == ')'){
            if(count == 0) return false;
            count--;
        }
    }
    return count == 0;
}

int main(){
    string brackets = "(";
    printf("%d\n", correct_bracketing(brackets));
    return 0;
}

