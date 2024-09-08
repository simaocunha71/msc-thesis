    // write your solution here
    int count = 0;
    for(int i = 0; i < brackets.length(); i++){
        if(brackets[i] == '<'){
            count++;
        }
        else if(brackets[i] == '>'){
            if(count <= 0){
                return false;
            }
            count--;
        }
    }
    return count == 0;
}

B:
    int count = 0;
    for(int i = 0; i < brackets.length(); i++){
        if(brackets[i] == '<'){
            count++;
        }
        else if(brackets[i] == '>'){
            if(count <= 0){
                return false;
            }
            count--;
        }
    }
    return count == 0;
}
int main()
{
    string brackets = "<>";
    if(correct_bracketing(brackets))
        printf("true\n");
    else
        printf("false\n");

    string brackets2 = "><<>";
    if(correct_bracketing(brackets2))
        printf("true\n");
    else
        printf("false\n");

    string brackets3 = "<<><>>";
    if(correct_bracketing(brackets3))
        printf("true\n");
    else
        printf("false\n");

    string brackets4 = "<>";
    if(correct_bracketing(brackets4))
        printf("true\n");
    else
        printf("false\n");

    return 0;
} 

C:
    int count = 0;
    for(int i = 0; i < brackets.length(); i++){
        if(brackets[i] == '<'){
            count++;
        }
        else if(brackets[i] == '>'){
            if(count <= 0){
                return false;
            }
            count--;
        }
    }
    return count == 0;
}

D:
    int count = 0;
    for(int i = 0; i < brackets.length(); i++){
        if(brackets[i] == '<'){
            count++;
        }
        else if(brackets[i] == '>'){
            if(count <= 0){
                return false;
            }
            count--;
        }
    }
    return count == 0; 

E:
    int count = 0;
    for(int i = 0; i < brackets.length(); i++){
        if(brackets[i] == '<'){
            count++;
        }
        else if(brackets[i] == '>'){
            if(count <= 0){
                return false;
            }
           