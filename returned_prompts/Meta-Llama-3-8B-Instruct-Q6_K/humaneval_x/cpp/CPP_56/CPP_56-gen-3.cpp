    int count = 0;
    for(int i = 0; i < brackets.size(); i++){
        if(brackets[i] == '<'){
            count++;
        }else if(brackets[i] == '>'){
            if(count == 0) return false;
            count--;
        }
    }
    return count == 0;
}

int main(){
    printf("%d\n", correct_bracketing("<")); //0
    printf("%d\n", correct_bracketing("<>")); //1
    printf("%d\n", correct_bracketing("<<><>>")); //1
    printf("%d\n", correct_bracketing("><<>")); //0
    return 0;
}

