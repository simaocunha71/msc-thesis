    int count = 0;
    for(char &c : brackets){
        if(c == '<'){
            count++;
        }else if(c == '>'){
            if(count == 0){
                return false;
            }
            count--;
        }
    }
    return count == 0;
}

int main(){
    printf("%d\n",correct_bracketing("<"));
    printf("%d\n",correct_bracketing("<>"));
    printf("%d\n",correct_bracketing("<<><>>"));
    printf("%d\n",correct_bracketing("><<>"));
    return 0;
}

*/
int main(){
    printf("%d\n",correct_bracketing("<"));
    printf("%d\n",correct_bracketing("<>"));
    printf("%d\n",correct_bracketing("<<><>>"));
    printf("%d\n",correct_bracketing("><<>"));
    return 0;
}

//src/main/resources/solutions/10123.cpp
