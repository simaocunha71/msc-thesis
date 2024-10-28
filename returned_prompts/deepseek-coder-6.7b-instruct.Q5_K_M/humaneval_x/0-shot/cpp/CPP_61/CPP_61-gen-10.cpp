    int n = brackets.length();
    int count = 0;
    for(int i = 0; i < n; i++){
        if(brackets[i] == '('){
            count++;
        }
        else if(brackets[i] == ')'){
            count--;
            if(count < 0){
                return false;
            }
        }
    }
    return count == 0;
}

int main()
{
    printf("%d\n", correct_bracketing("(")); //false
    printf("%d\n", correct_bracketing("()")); //true
    printf("%d\n", correct_bracketing("(()())")); //true
    printf("%d\n", correct_bracketing(")(()")); //false
    return 0;
}
*/

/*
